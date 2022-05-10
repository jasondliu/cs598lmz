import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os

# Import the Python wrapper module
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "lib"))
import lib_openmpt

# Load libopenmpt
libopenmpt_module = ctypes.CDLL(lib_openmpt.libopenmpt_path)

# Initialize libopenmpt
libopenmpt_module.openmpt_free_string.restype = None
libopenmpt_module.openmpt_free_string.argtypes = [ ctypes.c_char_p ]
libopenmpt_module.openmpt_get_library_version.restype = ctypes.c_char_p
libopenmpt_module.openmpt_get_library_version.argtypes = []
libopenmpt_module.openmpt_get_string.restype = ctypes.c_char_p
libopenmpt_module.openmpt_get_string.argtypes = [ ctypes.c_void_
