import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db")

import socket

###############################################################################

# This is not the most efficient way because it forces Python to load the
# library twice.

_has_pyrt = False

libpyrt = None

try:
    if 'nt' in os.name:
        libpyrt = ctypes.CDLL("pyrt.dll")
    else:
        lib = ctypes.util.find_library("pyrt")
        libpyrt = ctypes.CDLL(lib)
        
    _has_pyrt = True
except Exception as e:
    pass

###############################################################################

class _PyRT:
    """
    The class that implements the actual interface.
    This class is created by the Module, but should not be accessed directly.
    """

    def __init__(self, module):
        """
        Initializes the internal state of the module.
        The module parameter is a reference to the global module object.
        """

        global libpyrt

        self.module = module

        # Initialize
