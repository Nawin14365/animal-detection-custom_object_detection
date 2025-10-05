import cv2
from ultralytics import YOLO

# Load the trained YOLOv8 model
model = YOLO('D:/Ai_models_for_naac/Animal_detection/models/animal.pt')  # Update with your model path

# Initialize webcam
cap = cv2.imread("images_&_videos/fox.jpg") # 0 for the default webcam, change if you have multiple cameras
result = model(cap)
annotated_frame = result[0].plot()  # Draw bounding boxes on the frame
    # Display the resulting frame
cv2.imshow('YOLOv8 Real-Time Inference', annotated_frame)
# Check if the webcam is opened correctly
cv2.waitKey(0)