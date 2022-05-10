import ctypes
import ctypes.util
import threading
import sqlite3
import os
from os import path
import logging
import sys
import time
import re

# Load the C lib
lib_name = ctypes.util.find_library("sqlite3")
lib = ctypes.CDLL(lib_name)

# Some constants
SQLITE_TRANSIENT = ctypes.c_void_p(-1)
SQLITE_OK = 0
SQLITE_ROW = 100
SQLITE_DONE = 101

# Callback types
StepCallback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_char_p))
FinalCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

# Open a DB connection
_open = lib.sqlite3_open
_open.restype = ctypes.c_int
