import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

#==============================================================================
#   IMPORT
#==============================================================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg
import matplotlib.colors as colors

import time
import datetime
import cv2
import os

from skimage import io
from skimage import color
from skimage import filters
from skimage import morphology
from skimage import measure

#==============================================================================
#   FUNCTIONS
#==============================================================================

def get_frame(cap, scaling_factor):
    # Capture the frame from video capture object
    ret, frame = cap.read()
    
    # Resize the input frame
    frame = cv2.resize(frame, None, fx=scaling_factor, 
            fy=scaling_factor, interpolation=cv2.INTER_AREA)
    
    return frame

def convert_to_grey_
