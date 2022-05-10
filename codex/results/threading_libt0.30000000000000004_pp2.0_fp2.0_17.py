import threading
threading.Thread(target=lambda: None).start()

# Import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import os
import glob
import sys
import time
import RPi.GPIO as GPIO
import datetime
import subprocess
import pygame
import pygame.camera
import pygame.image
import pygame.surfarray

# Import the PCA9685 module.
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Define a function to set servo angle
def set_serv
