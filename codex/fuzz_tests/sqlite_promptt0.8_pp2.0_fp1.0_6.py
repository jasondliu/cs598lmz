import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)
import os.path
import platform
import time
import sqlite3
import uuid
import inspect
import logging
import random

# Note: python3 uses the frame locals, python2 uses the builtins
if sys.version_info >= (3, 0):
    import _thread
    import builtins
else:
    import __builtin__ as builtins

__all__ = ['threaded', 'enable_shared_cache']
__author__ = 'Randall Leeds'

# Set this to True to print cache contents. Useful for debugging.
TRACE = False

# Set this to True to see a bunch of debug messages.
DEBUG = False

if sys.version_info >= (3, 0):
    def _loadLibrary(name):
        libname = ctypes.util.find_library(name)
        if libname is None:
            return None
        return ctypes.CDLL(libname)
else:
    def _loadLibrary(name):
        return ctypes.CDLL(ct
