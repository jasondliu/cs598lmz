import ctypes
import ctypes.util
import threading
import sqlite3
import time
import logging
import _thread

# Load the library
_lib = ctypes.CDLL(ctypes.util.find_library('c'))

# Define the prototype for the function we use from the library
_lib.rand.restype = ctypes.c_int

def _get_random():
    """
    This is the actual function that is called for every
    random number.
    """
    return _lib.rand()

class Random(object):
    """
    This class is a wrapper around the C function rand().
    """
    def __init__(self):
        self.lock = threading.Lock()

    def rand(self):
        """
        This method calls the rand() function and then returns
        the result.
        """
        with self.lock:
            return _get_random()

# Create the global Random object
_random = Random()

def rand():
    """
    This is the function that the user calls.
    """
    return _random.rand()

