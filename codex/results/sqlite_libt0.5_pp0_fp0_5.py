import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import logging
import re
import sys

logger = logging.getLogger("rpi_rf")

# load the shared library
librf = ctypes.CDLL(ctypes.util.find_library("librf"))

# define the datatypes
librf.rf_init.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
librf.rf_init.restype = ctypes.c_int
librf.rf_send.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
librf.rf_send.restype = ctypes.c_int
librf.rf_cleanup.argtypes = []
librf.rf_cleanup.restype = None

# define the exception
class RfException(Exception):
    pass

class RfDevice(object):
    """A base class for all devices"""
    def __init__(self, pin
