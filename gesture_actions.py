import subprocess
import cv2


def volume_up():
    subprocess.run(
        [
            "pactl",
            "set-sink-volume",
            "@DEFAULT_SINK@",
            "+5%"
        ],
        check=False
    )


def volume_down():
    subprocess.run(
        [
            "pactl",
            "set-sink-volume",
            "@DEFAULT_SINK@",
            "-5%"
        ],
        check=False
    )


def take_screenshot(frame, timestamp):
    filename = f"screenshot_{int(timestamp)}.png"
    cv2.imwrite(filename, frame)

    print(f"Screenshot saved: {filename}")

    return filename


def perform_action(gesture, frame, current_time):
    if gesture == "THUMBS UP":
        volume_up()
        return "Volume Up"

    elif gesture == "THUMBS DOWN":
        volume_down()
        return "Volume Down"

    elif gesture == "TWO FINGERS":
        take_screenshot(frame, current_time)
        return "Screenshot"

    elif gesture == "FIST":
        return "Fist Detected"

    elif gesture == "ONE FINGER":
        return "One Finger"

    elif gesture == "OPEN PALM":
        return "Open Palm"

    elif gesture == "NO HAND":
        return "Waiting..."

    return gesture
