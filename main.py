import cv2
import mediapipe as mp
import time
import subprocess
from gesture_detector import detect_gesture


# -----------------------------
# MediaPipe Hands
# -----------------------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)


# -----------------------------
# Webcam
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


# -----------------------------
# Variables
# -----------------------------
last_action_time = 0
cooldown = 1.0

current_time = 0
fps = 0
prev_time = time.time()

action = "None"


# -----------------------------
# Main Loop
# -----------------------------
while True:

    success, frame = cap.read()

    if not success:
        print("Could not read frame.")
        break

    # Mirror webcam
    frame = cv2.flip(frame, 1)

    # Get frame dimensions
    h, w, c = frame.shape

    # Convert BGR -> RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb_frame)

    gesture = "NO HAND"

    # -----------------------------
    # Process detected hand
    # -----------------------------
    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            # Draw hand landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Convert landmarks to simple coordinates
            landmarks = []

            for landmark in hand_landmarks.landmark:
                x = int(landmark.x * w)
                y = int(landmark.y * h)

                landmarks.append((x, y))

            # Detect gesture
            gesture = detect_gesture(landmarks)

    else:
        gesture = "NO HAND"


    # -----------------------------
    # Current time
    # -----------------------------
    current_time = time.time()


    # -----------------------------
    # THUMBS UP = Volume Up
    # -----------------------------
    if gesture == "THUMBS UP":

        action = "Volume Up"

        if current_time - last_action_time > cooldown:

            subprocess.run(
                [
                    "pactl",
                    "set-sink-volume",
                    "@DEFAULT_SINK@",
                    "+5%"
                ]
            )

            last_action_time = current_time


    # -----------------------------
    # THUMBS DOWN = Volume Down
    # -----------------------------
    elif gesture == "THUMBS DOWN":

        action = "Volume Down"

        if current_time - last_action_time > cooldown:

            subprocess.run(
                [
                    "pactl",
                    "set-sink-volume",
                    "@DEFAULT_SINK@",
                    "-5%"
                ]
            )

            last_action_time = current_time


    # -----------------------------
    # TWO FINGERS = Screenshot
    # -----------------------------
    elif gesture == "TWO FINGERS":

        action = "Screenshot"

        if current_time - last_action_time > cooldown:

            filename = (
                f"screenshot_"
                f"{int(current_time)}.png"
            )

            cv2.imwrite(filename, frame)

            print(f"Screenshot saved: {filename}")

            last_action_time = current_time


    # -----------------------------
    # Other gestures
    # -----------------------------
    elif gesture == "FIST":

        action = "Fist Detected"


    elif gesture == "ONE FINGER":

        action = "One Finger"


    elif gesture == "OPEN PALM":

        action = "Open Palm"


    elif gesture == "NO HAND":

        action = "Waiting..."


    else:

        action = gesture


    # -----------------------------
    # FPS calculation
    # -----------------------------
    now = time.time()

    fps = 1 / (now - prev_time)

    prev_time = now


    # -----------------------------
    # Information Box
    # -----------------------------
    cv2.rectangle(
        frame,
        (20, 20),
        (350, 145),
        (0, 0, 0),
        -1
    )

    cv2.putText(
        frame,
        f"Gesture: {gesture}",
        (35, 55),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Action: {action}",
        (35, 85),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (35, 115),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )


    # -----------------------------
    # Show frame
    # -----------------------------
    cv2.imshow(
        "AI Hand Gesture Controller",
        frame
    )


    # -----------------------------
    # Press Q to quit
    # -----------------------------
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break


# -----------------------------
# Cleanup
# -----------------------------
cap.release()
hands.close()
cv2.destroyAllWindows()
