import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# Imports
import RPi.GPIO as GPIO
import time
import math
import numpy as np
import csv
from collections import deque
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import serial

# Initialize variables

data = [1,1,1,1,1]

# Initialize GPIO port

GPIO.setmode(GPIO.BCM)

# Initialize the serial port

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
)

# Configure GPIO pins

GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

