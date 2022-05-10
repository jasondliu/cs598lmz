import threading
# Test threading daemon
from time import sleep
import datetime
from tkinter import Tk, Label, font
from tkinter.ttk import Style

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib.animation import FuncAnimation

from imu import IMU
from pid_imu import Controller_PID
from PIL import Image, ImageTk

# ===============================================================================
# Execute if running on RasPi
if not sys.platform.startswith('win32'):
    # Load primary class object
    import RPi.GPIO as GPIO
    import smbus    # for I2C communications
    from Adafruit_I2C import Adafruit_I2C
    # Load secondary classes
    from adafruit7seg.pca9554driver import PCA9554Driver  # 7-Segment Display
    from adafruit7seg.examples.example7seg import Example7Seg
    from input import Input
    from db import Server
    from power_button import PowerState
   
