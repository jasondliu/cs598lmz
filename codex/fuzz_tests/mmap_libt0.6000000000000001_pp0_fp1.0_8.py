import mmap
import os
import sys
import time
import wave
import struct

# This code is based on the following:
# https://github.com/adafruit/Adafruit_Python_PCA9685/blob/master/Adafruit_PCA9685/PCA9685.py
# https://github.com/adafruit/Adafruit_Python_PCA9685/blob/master/examples/servo_simpletest.py

# Define a function to convert a value to the number of steps needed
# to set the servo to that value.
def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Import the PCA9685 module.
import Adafruit_PCA9685

# Initialise the PCA9685 using the
