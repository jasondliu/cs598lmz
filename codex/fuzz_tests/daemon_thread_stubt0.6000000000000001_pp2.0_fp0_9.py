import sys, threading

def run():
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def get_frame(cap):
    while True:
        ret, frame = cap.read()
        if ret:
            yield frame
        else:
            break

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    threading.Thread(target = run).start()
    for frame in get_frame(cap):
        cv2.imshow('frame', frame)
