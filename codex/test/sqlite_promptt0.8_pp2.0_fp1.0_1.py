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
