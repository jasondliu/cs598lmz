import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H")).start()

# Import the necessary packages
from imutils.video import VideoStream
from imutils import face_utils
import imutils
import time
import dlib
import cv2
import numpy as np
import os
import math
import datetime

# Initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Initialize the video stream and allow the cammera sensor to warmup
print("[INFO] camera sensor warming up...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# Initialize the frame counters and the total number of blinks
COUNTER = 0
TOTAL = 0

# Initialize the dictionary that maps the indexes of the facial

