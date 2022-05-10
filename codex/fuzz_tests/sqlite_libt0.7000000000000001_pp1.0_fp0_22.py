import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

# This is a port of the C sample code to python.
# Do not try to run this code in the same program as the C code.

# This is the only library we need to import.
# Note that we have to call it '_lib_' because there is already a
# library called 'lib' in python.
_lib_ = ctypes.cdll.LoadLibrary(ctypes.util.find_library("libhidapi-hidraw"))

# Some constants
HID_MAX_DESCRIPTOR_SIZE = 4096

# Some ctypes stuff
_lib_.hid_init.argtypes = []
_lib_.hid_init.restype = None

_lib_.hid_exit.argtypes = []
_lib_.hid_exit.restype = None

_lib_.hid_enumerate.argtypes = [ctypes.c_ushort, ctypes.c_ushort]
_lib_.hid_enumerate.restype = ctypes.POINTER(ctypes.c_ubyte)

_lib_.hid_free_enumer
