import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

from . import _sqlite3

# This is a hack to get around the fact that ctypes.util.find_library
# doesn't know about .dylib suffix on OS X.
if sys.platform == 'darwin':
    ctypes.util.find_library = lambda x: ctypes.util.find_library(x) or ctypes.util.find_library(x + '.dylib')

# Load the shared library.
lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

# Set up the return types.
lib.sqlite3_open.restype = ctypes.c_int
lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
lib.sqlite3_close.restype = ctypes.c_int
lib.sqlite3_close.argtypes = [ctypes.c_void_p]
lib.sqlite3_prepare_v2
