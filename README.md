# 🦁 Animal Detection using YOLOv8

A simple yet powerful animal detection system that can identify animals in both images and video streams using YOLOv8. Perfect for wildlife monitoring, security systems, or educational purposes.

## 🚀 Quick Start

1. **Clone this repository**
```bash
git clone [your-repository-url]
cd Animal_detection
```

2. **Download the models**
- Visit our [Google Drive folder](https://drive.google.com/drive/folders/1zeTcCzYGSdk_n3pUnNU9a2_fL3hWq2P8?usp=drive_link)
- Download both model files (`animal.pt` and `animal2.pt`)
- Create a `models` folder in your project directory
- Place the downloaded model files in the `models` folder

3. **Install requirements**
```bash
pip install -r requirements.txt
```

4. **Run the detection**
- For images:
```bash
python animal_detection_image.py
```
- For videos:
```bash
python animal_detection.py
```

## 🎯 Features

- 📸 Detect animals in static images
- 🎥 Real-time detection in videos
- 🎮 Easy-to-use interface
- 🔄 Support for multiple video formats
- 🎯 Adjustable detection confidence

## 📋 Requirements

- Python 3.7+
- OpenCV (cv2)
- Ultralytics YOLOv8
- Other dependencies (listed in requirements.txt)

## 📁 Project Structure

```
Animal_detection/
├── animal_detection.py        # Video detection script
├── animal_detection_image.py  # Image detection script
├── models/                    # Place downloaded models here
└── images_&_videos/          # Sample media files
```

## 🛠️ Usage Guide

1. Clone this repository:
```bash
git clone [your-repository-url]
cd Animal_detection
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Image Detection
1. Open `animal_detection_image.py`
2. Update the image path if needed:
```python
cap = cv2.imread("images_&_videos/your_image.jpg")
```
3. Run the script
4. Press any key to close the detection window

### Video Detection
1. Open `animal_detection.py`
2. Update the video source if needed:
```python
cap = cv2.VideoCapture("images_&_videos/your_video.mp4")  # For video file
# OR
cap = cv2.VideoCapture(0)  # For webcam
```
3. Run the script
4. Press 'q' to quit

## ⬇️ Getting the Models

The model files are too large for GitHub (>25MB), so they're hosted on Google Drive:

1. Access the models here: [Download Models](https://drive.google.com/drive/folders/1zeTcCzYGSdk_n3pUnNU9a2_fL3hWq2P8?usp=drive_link)
2. Download both files:
   - `animal.pt` (Primary model)
   - `animal2.pt` (Alternative model)
3. Create a `models` directory in your project
4. Place the downloaded files in the `models` directory

## 🔧 Configuration

You can modify these parameters in the scripts:
- Confidence threshold (default: 0.5)
- Input source (webcam/video file/image)
- Model path

Example:
```python
results = model(frame, conf=0.5)  # Adjust confidence threshold here
```

## 🆘 Need Help?

If you encounter any issues:
1. Check if the models are correctly placed in the `models` folder
2. Verify all dependencies are installed
3. Make sure input paths to images/videos are correct
4. Create an issue in the repository if the problem persists

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.