import cv2
from ultralytics import YOLO

# Load the trained YOLOv8 model
model = YOLO('D:/Ai_models_for_naac/Animal_detection/models/animal.pt')  # Update with your model path

# Initialize webcam or video file
cap = cv2.VideoCapture("images_&_videos/Fox Sound.mp4")  # 0 for the default webcam, change if you have multiple cameras

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Perform inference with a specified confidence threshold
    results = model(frame, conf=0.5)  # Adjust confidence level as needed (0.5 is an example)

    # Process the results
    annotated_frame = results[0].plot()  # Draw bounding boxes on the frame

    # Display the resulting frame
    cv2.imshow('YOLOv8 Real-Time Inference', annotated_frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
