import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Import the necessary packages
from pyimagesearch.tempimage import TempImage
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import warnings
import datetime
import imutils
import json
import time
import cv2
import numpy as np
import os
import sys
import RPi.GPIO as GPIO

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
