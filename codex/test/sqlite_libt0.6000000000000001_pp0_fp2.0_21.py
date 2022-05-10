import ctypes
import ctypes.util
import threading
import sqlite3
import os
import logging
import datetime
import time

# This is a very simple example of how you can use the c library
# you can even do this in C, but I wanted to show how it can be done in python
#
# This is not a full example, there are a lot of things you can do, but this is just a quick example

# the structs are defined in the c library

class WifiScan(ctypes.Structure):
    _fields_ = [
        ("device", ctypes.c_char_p),
        ("timestamp", ctypes.c_longlong),
        ("mac", ctypes.c_char_p),
        ("signal_level", ctypes.c_int)
    ]

class WifiScanList(ctypes.Structure):
    _fields_ = [
        ("scans", ctypes.POINTER(WifiScan)),
        ("length", ctypes.c_int)
    ]

# Load the library, you will need to change the path to where you have it
