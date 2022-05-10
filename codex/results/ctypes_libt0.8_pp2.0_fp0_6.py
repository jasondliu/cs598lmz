import ctypes
ctypes.windll.user32.SetProcessDPIAware()
import cv2

def get_frame(video_path, scale=1):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, None, fx=scale, fy=scale)
        yield frame
    cap.release()
    cv2.destroyAllWindows()

def draw(frame, people, output_size):
    frame_h, frame_w = frame.shape[:2]
    for person in people:
        for joint in person:
            x, y, z = joint
            if z > 0:
                cv2.circle(frame, (int(x * frame_w), int(y * frame_h)), 5, (0, 255, 0), -1)
    frame = cv2.resize(frame, output_size)
    return frame

def main():
    input_size = (640, 480
