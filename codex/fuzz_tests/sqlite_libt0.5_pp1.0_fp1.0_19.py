import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import subprocess
import datetime
import re

from ctypes import *

# These are the required functions that are needed to be loaded
# from the library.

# Get the library path
_lib = ctypes.util.find_library('c')
_libc = ctypes.CDLL(_lib, use_errno=True)

# Get the prototypes of the required functions
_libc.clock_gettime.argtypes = [c_int, POINTER(timespec)]
_libc.clock_gettime.restype = c_int
_libc.clock_settime.argtypes = [c_int, POINTER(timespec)]
_libc.clock_settime.restype = c_int
_libc.clock_getres.argtypes = [c_int, POINTER(timespec)]
_libc.clock_getres.restype = c_int

# Initialize the time constants
CLOCK_REALTIME = 0
CLOCK_MONOTONIC = 1
CLOCK_MONOTONIC_
