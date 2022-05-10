import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

# This is the list of all the registered functions
# that can be called from the C library.
_FUNCTIONS = []

def _register_function(f):
    """Decorator used to register a function in the C library."""
    _FUNCTIONS.append(f)
    return f

# The C library is loaded lazily.
_LIB = None

def _load_lib():
    """Load the C library."""
    global _LIB
    if _LIB is None:
        _LIB = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
        _LIB.sqlite3_initialize()
        _LIB.sqlite3_enable_shared_cache(0)
        _LIB.sqlite3_config(ctypes.c_int(1), ctypes.c_int(0))
        _LIB.sqlite3_config(ctypes.c_int(2), ctypes.c_int(0))
