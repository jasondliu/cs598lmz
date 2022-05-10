import mmap
import sys
import time
import os
import numpy as np
import cv2

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 %s <video_file>" % sys.argv[0])
        sys.exit(1)

    cap = cv2.VideoCapture(sys.argv[1])
    if not cap.isOpened():
        print("Error opening video stream or file")
        sys.exit(1)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
