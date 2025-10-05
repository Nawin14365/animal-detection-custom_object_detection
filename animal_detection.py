
import os
from flask import Flask, request, render_template, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename
import cv2
import numpy as np
from ultralytics import YOLO

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp4', 'avi', 'mov'}
MODEL_PATH = 'models/animal.pt'

# Create upload folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'your_secret_key'  # Change for production

# Load YOLOv8 model
model = YOLO(MODEL_PATH)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def annotate_image(image_path):
    image = cv2.imread(image_path)
    results = model(image, conf=0.5)
    annotated = results[0].plot()
    output_path = os.path.join(UPLOAD_FOLDER, 'annotated_' + os.path.basename(image_path))
    cv2.imwrite(output_path, annotated)
    return output_path

def annotate_video(video_path):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_path = os.path.join(UPLOAD_FOLDER, 'annotated_' + os.path.basename(video_path))
    out = None
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame, conf=0.5)
        annotated_frame = results[0].plot()
        out.write(annotated_frame)
    cap.release()
    out.release()
    return output_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            ext = filename.rsplit('.', 1)[1].lower()
            if ext in {'png', 'jpg', 'jpeg'}:
                annotated_path = annotate_image(file_path)
                return send_file(annotated_path, mimetype='image/jpeg')
            else:
                annotated_path = annotate_video(file_path)
                return send_file(annotated_path, mimetype='video/mp4')
        else:
            flash('File type not allowed')
            return redirect(request.url)
    return '''
    <!doctype html>
    <title>Animal Detection Upload</title>
    <h1>Upload Image or Video for Animal Detection</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
