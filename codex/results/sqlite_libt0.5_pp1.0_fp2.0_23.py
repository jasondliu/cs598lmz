import ctypes
import ctypes.util
import threading
import sqlite3
import os
from os.path import expanduser
from datetime import datetime
from random import randint
from time import sleep
from sys import exit
import requests
import signal
import sys
from pprint import pprint
from subprocess import Popen, PIPE

# Set up ctypes for Windows
if os.name == 'nt':
    windll = ctypes.windll.kernel32
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    SCREEN_WIDTH = user32.GetSystemMetrics(0)
    SCREEN_HEIGHT = user32.GetSystemMetrics(1)

# Set up ctypes for OSX
if os.name == 'posix':
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    libc.sysctl.argtypes = [ctypes.c_int, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t]
   
