import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys

from . import tty

try:
    from . import x11
except ImportError:
    x11 = None

# Workaround for libc and python3 incompatibility
if sys.version_info.major >= 3:
    _ctypes_python3 = True
    ctypes.pythonapi.PyString_AsStringAndSize.argtypes = [ctypes.py_object,
                                                          ctypes.POINTER(ctypes.c_char_p),
                                                          ctypes.POINTER(ctypes.c_size_t)]
else:
    _ctypes_python3 = False
    ctypes.pythonapi.PyString_AsStringAndSize.argtypes = [ctypes.py_object,
                                                          ctypes.POINTER(ctypes.c_char_p),
                                                          ctypes.POINTER(ctypes.c_int)]


libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))

# https://github.com/torvalds/
