import sys, threading

def run():
    global exit
    while True:
        if exit:
            break
        if state:
            cv2.imshow("Video", frame)
            cv2.waitKey(1)

def get_frame():
    global frame
    while True:
        ret, frame = cap.read()
        if not ret:
            break

if __name__ == "__main__":
    cap = cv2.VideoCapture(sys.argv[1])
    cv2.namedWindow("Video")
    frame_thread = threading.Thread(target=get_frame)
    frame_thread.start()

    run_thread = threading.Thread(target=run)
    run_thread.start()

    run_thread.join()
