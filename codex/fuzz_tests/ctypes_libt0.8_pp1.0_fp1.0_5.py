import ctypes
ctypes.windll.user32.SetProcessDPIAware() #move to class constructor: self.SetProcessDPIAware()

# import the necessary packages
import numpy as np
import cv2
import win32api, win32con
import time
import pyautogui
import ctypes

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# For debugging
import matplotlib.pyplot as plt

# Create a vision client and connect to google cloud
client = vision.ImageAnnotatorClient()


# Define constants and set values
RESOLUTION_X = int(1920/2)
RESOLUTION_Y = int(1080/2)

DISPLAY_X = int(win32api.GetSystemMetrics(0))/2
DISPLAY_Y = int(win32api.GetSystemMetrics(1))/2

# Calculate how wide the window is based on the resolution set
MAX_WIDTH = int(DISPLAY_X - RESOLUTION_X)
MAX_HEIGHT = int(DISPLAY_
