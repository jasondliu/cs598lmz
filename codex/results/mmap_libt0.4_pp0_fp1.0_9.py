import mmap
import numpy as np
import time
from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import sys
import cv2
import logging
from logging.handlers import RotatingFileHandler

# Set up logger
logger = logging.getLogger('detect_face')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('detect_face_log.txt', maxBytes=10*1024*1024, backupCount=5)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Set up camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# Load the model
net = cv2.dnn.readNetFrom
