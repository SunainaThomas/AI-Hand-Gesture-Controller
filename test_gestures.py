from utils import display_gesture

def test_gesture_detection():
    result = display_gesture("thumbs_up")
    assert result == "Detected Gesture: thumbs_up"

def test_no_gesture():
    result = display_gesture(None)
    assert result == "No gesture detected"

if __name__ == "__main__":
    test_gesture_detection()
    test_no_gesture()
    print("All tests passed!")
