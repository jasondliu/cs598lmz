import sys, threading

def run():
    # Use globals because this function is executed in a separate thread.
    global frame, is_shutdown
    while not is_shutdown:
        frame = get_frame()
    print("Stopping capture thread...")

def get_frame():
    ret, frame = cap.read()
    if not ret:
        print("ERROR: Unable to read camera frame!")
        exit()
    return resize(frame, (320, 240))

def get_image():
    # Return next image from camera
    return frame

def shutdown():
    global is_shutdown
    is_shutdown = True
    # Wait for thread to end and release camera
    thread.join()
    cap.release()

# Initialize camera
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if not ret:
    print("ERROR: Unable to read camera frame!")
    exit()
frame = resize(frame, (320, 240))
is_shutdown = False
thread = threading.Thread(target=run)
thread.start()
