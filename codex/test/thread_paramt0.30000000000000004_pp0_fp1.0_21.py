import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# Import libraries
import numpy as np
import cv2
import time
import os
import sys
import argparse
import imutils
import math
import serial
import datetime
import csv

# Import files
import functions as fun
import constants as const

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="Serial port to use")
parser.add_argument("-f", "--file", help="File to save data to")
parser.add_argument("-t", "--time", help="Time to run program in seconds")
parser.add_argument("-c", "--camera", help="Camera to use")
args = parser.parse_args()

# Set up serial port
if args.port:
    ser = serial.Serial(args.port, 9600, timeout=0.1)
else:
    ser = serial.Serial('COM3', 9600, timeout=0.1)
