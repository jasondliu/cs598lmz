import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

# import the necessary packages
import numpy as np
import cv2
import time
import math
import matplotlib.pyplot as plt
import sys

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# open webcam video stream
cap = cv2.VideoCapture(0)

# the output will be written to output.avi
out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (640,480))

# loop over frames from the video stream
while(cap.isOpened()):
    # read the next frame from the file
    (grabbed, frame) = cap.read()

    # if the frame was not grabbed, then we have reached the end
    # of the stream
    if not grabbed:
        break

    # resize the frame and
