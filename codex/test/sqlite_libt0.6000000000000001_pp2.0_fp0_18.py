import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import re
import ConfigParser
import sys
import socket

from time import sleep



# Constants

# DB
DATABASE_LOCATION = '/home/pi/logs/log.db'

# GPIO
MOTION_PIN = 2

# GPIO Modes
GPIO_INPUT = 0
GPIO_OUTPUT = 1

# GPIO Values (Logical)
GPIO_LOW = 0
GPIO_HIGH = 1

GPIO_LOW_STR = "LOW"
GPIO_HIGH_STR = "HIGH"

# GPIO Values (Physical)
GPIO_PHYS_LOW = 0
GPIO_PHYS_HIGH = 1

# GPIO Pull Up/Down
GPIO_PUD_OFF = 0
GPIO_PUD_DOWN = 1
GPIO_PUD_UP = 2

# GPIO Edge Detect
GPIO_RISING_EDGE = 0
GPIO_FALLING_EDGE = 1
GPIO_BOTH_EDGE = 2

# GPIO
