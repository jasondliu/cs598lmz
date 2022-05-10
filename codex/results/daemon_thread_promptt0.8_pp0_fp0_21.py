import threading
# Test threading daemon
x = threading.Event()
 
def foo():
    while True:
        x.wait()
        print "Start!"
        x.clear()
 
t = threading.Thread(target=foo)
t.start()
x.set()

# Module for processing video streams
from pyimagesearch.centroidtracker import CentroidTracker
from pyimagesearch.trackableobject import TrackableObject
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2

# Module for detecting collisions
from pyimagesearch.detection import collision
