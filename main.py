import cv2
import mediapipe as mp
import time

from gesture_detector import detect_gesture
from gesture_actions import perform_action
from config import (
    CAMERA_INDEX,
    DETECTION_CONFIDENCE,
    TRACKING_CONFIDENCE,
    ACTION_COOLDOWN,
    WINDOW_NAME
)
from utils import calculate_fps, draw_information


# ==========================================
# MediaPipe Hands Setup
# ==========================================

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
