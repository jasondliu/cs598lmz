import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import sys
import os.path
con = None

# path = os.path.realpath(__file__)
# path = os.path.abspath(os.path.join(os.path.split(path)[0], os.path.pardir)
# path = os.path.join(path, "..", "static")
# path = os.path.abspath(path)
# print path
# sys.path.insert(0, path)

# Get the DLL's path according to its name
_libraries = {}
_libraries['libhoughtemplateimage.so'] = ctypes.CDLL('libhoughtemplateimage.so')

# Load the DLL
_lib = _libraries['libhoughtemplateimage.so']

# Some functions need to be told explicitly that the arguments may be modified.
_lib.hough_template_match.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.
