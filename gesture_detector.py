import math


def distance(point1, point2):
    return math.sqrt(
        (point1[0] - point2[0]) ** 2 +
        (point1[1] - point2[1]) ** 2
    )


def detect_gesture(landmarks):
    """
    Detect basic hand gestures using MediaPipe landmarks.

    Landmark indexes:
    4  - Thumb tip
    8  - Index tip
    12 - Middle tip
    16 - Ring tip
    20 - Pinky tip
    """

    # Finger states
    index_up = landmarks[8][1] < landmarks[6][1]
    middle_up = landmarks[12][1] < landmarks[10][1]
    ring_up = landmarks[16][1] < landmarks[14][1]
    pinky_up = landmarks[20][1] < landmarks[18][1]

    # Thumb direction
    thumb_up = landmarks[4][1] < landmarks[3][1]

    # Number of fingers raised
    fingers = sum([
        index_up,
        middle_up,
        ring_up,
        pinky_up
    ])

    # Open palm
    if fingers == 4:
        return "OPEN PALM"

    # Fist
    if fingers == 0 and not thumb_up:
        return "FIST"

    # Two fingers
    if index_up and middle_up and not ring_up and not pinky_up:
        return "TWO FINGERS"

    # One finger
    if index_up and not middle_up and not ring_up and not pinky_up:
        return "ONE FINGER"

    # Thumbs up
    if thumb_up and fingers == 0:
        return "THUMBS UP"

    return "UNKNOWN"
