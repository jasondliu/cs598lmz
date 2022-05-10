import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# Import the required modules
import cv2
import argparse
import numpy as np

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args['image'])

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Compute the Scharr gradient magnitude representation of the images
# in both the x and y direction using the OpenCV Sobel() function
gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
