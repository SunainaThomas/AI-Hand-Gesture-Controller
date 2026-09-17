# # AI Hand Gesture Controller

A real-time computer vision project that allows users to control computer functions using hand gestures through a webcam.

## Features

- 👍 Thumbs Up → Increase system volume
- 👎 Thumbs Down → Decrease system volume
- ✌️ Two Fingers → Take a screenshot
- ☝️ One Finger → Mouse control
- 🖐️ Open Palm → Neutral / Stop
- Real-time hand landmark detection
- FPS monitoring
- Webcam-based interaction

## Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI
- Linux PulseAudio/PipeWire (`pactl`)

## How It Works

The webcam captures live video frames.

MediaPipe detects the hand and extracts hand landmarks. The gesture detection module analyzes the landmark positions and identifies the user's gesture.

The detected gesture is then mapped to a computer action.

```text
Webcam
   ↓
OpenCV
   ↓
MediaPipe Hand Detection
   ↓
Hand Landmarks
   ↓
Gesture Recognition
   ↓
Computer Action
