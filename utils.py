import cv2


def calculate_fps(previous_time):
    current_time = __import__("time").time()

    fps = 1 / (current_time - previous_time)

    return current_time, fps


def draw_information(frame, gesture, action, fps):

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

    return frame
