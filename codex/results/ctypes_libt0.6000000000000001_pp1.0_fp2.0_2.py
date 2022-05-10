import ctypes
ctypes.cdll.LoadLibrary('/usr/local/lib/libopencv_core.so')
ctypes.cdll.LoadLibrary('/usr/local/lib/libopencv_imgproc.so')
ctypes.cdll.LoadLibrary('/usr/local/lib/libopencv_highgui.so')

import cv2

print(cv2.__version__)

img = cv2.imread('opencv-logo.png')

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

# import the necessary packages
from __future__ import print_function
from pyimagesearch.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image to be scanned")
args
