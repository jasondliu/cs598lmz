import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import datetime

# TODO:
# 1. Save the data in a database
# 2. Add a GUI
# 3. Add a way to set the filepath
# 4. Add a way to set the time interval
# 5. Add a way to set the time duration

# Global variables
filepath = ''
interval = 0
duration = 0

# Define the function to call the C library
def get_cpu_temp():
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    libc.sysconf.restype = ctypes.c_long
    libc.sysconf.argtypes = [ctypes.c_int]
    buf = ctypes.create_string_buffer(4096)
    libc.confstr(ctypes.c_int(89), buf, ctypes.c_int(4096))
    return float(buf.value)

# Define the function to save the data to a database
def save_data(filepath, interval, duration):
    # Initial
