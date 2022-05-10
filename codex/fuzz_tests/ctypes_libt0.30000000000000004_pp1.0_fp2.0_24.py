import ctypes
ctypes.cdll.LoadLibrary('/usr/local/lib/libopencv_core.so')
ctypes.cdll.LoadLibrary('/usr/local/lib/libopencv_imgproc.so')
ctypes.cdll.LoadLibrary('/usr/local/lib/libopencv_highgui.so')

import cv2
import numpy as np
import sys

# Read image given by user
im = cv2.imread(sys.argv[1])

# Convert image to grayscale
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Threshold the image
ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)

# Find contours in the image
ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get rectangles contains each
