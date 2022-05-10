import sys, threading
threading.Thread(target=lambda: sys.stderr.write('\x1b[2J\x1b[H')).start()

import cv2
import numpy as np
import time
import math

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

# create switch for ON/OFF functionality
switch2 = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch2, 'image',0,1,nothing)

# create switch for ON/OFF functionality
switch3 = '
