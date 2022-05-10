import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import os
import sys
import types
import tempfile
# Importing the multiprocessing module messes with threading.local()
# objects in a bad way.
import multiprocessing

try:
    import time
    current_time = time.time
except ImportError:
    import time
    if sys.platform == "win32":
        current_time = time.clock
    else:
        current_time = time.time


# Try to import the _sqlite module.
try:
    import _sqlite3
except ImportError:
    # Attempt to locate the _sqlite module by looking at sys.path,
    # sys.prefix, and sys.exec_prefix, and then trying to load it.
    # This is the same strategy used by ctypes.util.find_library() to
    # find and load a C library.
    for directory in sys.path + [sys.prefix, sys.exec_prefix]:
        try:
            file, pathname, description = imp.find_module('_sqlite3',[directory])
            _
