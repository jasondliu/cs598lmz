import mmap
import os
import sys
import time

# Importing Adafruit_BBIO library
sys.path.insert(0, "/usr/local/lib/python2.7/dist-packages")
from Adafruit_BBIO.SPI import SPI

# Importing the PyCRC library
sys.path.insert(0, "/home/debian/Desktop/PyCRC-1.7/src")
import crcmod

# Importing the PySerial library
sys.path.insert(0, "/home/debian/Desktop/pyserial-3.2.1")
import serial

# Importing the OSC library
sys.path.insert(0, "/home/debian/Desktop/pyOSC-0.3.5b_0.3.5b-8-g0f3c801/")
import OSC

# Open Serial Port of Arduino Micro
# baud rate: 115200
# timeout: 1 second
ser = serial.Serial(port = "/dev/ttyACM0", baudrate=115200, timeout = 1)

# Open txt file
