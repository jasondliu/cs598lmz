import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

import numpy as np
import numpy.ctypeslib as npct
import cv2

import cv2.aruco as aruco

import time

# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(18,GPIO.OUT)
# GPIO.setup(23,GPIO.OUT)
# GPIO.setup(24,GPIO.OUT)
# GPIO.setup(25,GPIO.OUT)

# GPIO.output(18,GPIO.HIGH)
# GPIO.output(23,GPIO.HIGH)
# GPIO.output(24,GPIO.HIGH)
# GPIO.output(25,GPIO.HIGH)

# GPIO.output(18,GPIO.LOW)
# GPIO.output(23,GPIO.LOW)
# GPIO.output(24,GPIO.LOW)
# GPIO.output(25,GPIO.LOW
