import threading
threading.stack_size(67108864)

# sys.setrecursionlimit(2 ** 20)

# numpy and scipy
import numpy
import scipy

# OpenCV
import cv2

# Serial
import serial
import time

# Raspberry Pi GPIO
import RPi.GPIO as GPIO

# TensorFlow
import tensorflow as tf

# Image classifier
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

# Initialize variables
frame = None
process_this_frame = True

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

# Set the mode of numbering the pins.
GPIO.setmode(GPIO.BCM)

# Set pins as output.
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


