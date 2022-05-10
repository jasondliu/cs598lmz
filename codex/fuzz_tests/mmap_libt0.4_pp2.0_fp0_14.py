import mmap
import os
import sys
import time

from datetime import datetime
from io import BytesIO
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from picamera import PiCamera
from picamera.array import PiRGBArray

# Set up camera constants
IM_WIDTH = 640
IM_HEIGHT = 480

# The camera is mounted upside down, so flip the image
# and flip the text
FLIP_IMAGE = True
FLIP_TEXT = True

# Set up camera constants
IM_WIDTH = 640    # Use smaller resolution for
IM_HEIGHT = 480   # slightly faster framerate

# Set up camera constants
IM_WIDTH = 640    # Use smaller resolution for
IM_HEIGHT = 480   # slightly faster framerate

# Select camera type (if user enters --usbcam when calling this script,
# a USB webcam will be used)
camera_type = 'picamera'

# This is needed since the working directory is the object_detection folder.
sys.path.append('..')

# Import util
