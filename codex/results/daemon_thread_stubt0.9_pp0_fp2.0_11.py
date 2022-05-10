import sys, threading

def run():

    caps = cv2.VideoCapture(sys.argv[1] if len(sys.argv)>1 else 0)

    while cv2.waitKey(1) < 0:
        r, img = caps.read()
        cv2.imshow('camera', img)

    cv2.destroyAllWindows()

threading.Thread(target=run).start()
