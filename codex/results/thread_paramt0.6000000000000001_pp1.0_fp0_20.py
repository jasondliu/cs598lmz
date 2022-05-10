import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()
from mvnc import mvncapi as mvnc
import cv2
import numpy
import time
import csv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Name of the opencv window
CV_WINDOW_NAME = "SSD MobileNet"

# Name of the opencv window
CV_WINDOW_NAME = "SSD MobileNet"

# Desired width and height of the network inputs
NETWORK_IMAGE_WIDTH = 300
NETWORK_IMAGE_HEIGHT = 300

# Variables to store the final detection results
total_time = 0
num_runs = 0

# ---- Step 1: Open the enumerated device and get a handle to it -------------

# Look for enumerated NCS device(s); quit program if none found.
devices = mvnc.EnumerateDevices()
if len( devices ) == 0:
	print( "No devices found" )
	quit()

# Get a handle to the first enumerated device and open it
