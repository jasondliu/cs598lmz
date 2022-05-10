import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import time
import json
import re

"""
This is a very simple Python script that turns test_id's into test_names.
It is a work in progress, and is certainly not production ready.
"""

# Load the libmozglue library in order to use its function(s)
libmozglue = ctypes.cdll.LoadLibrary(ctypes.util.find_library('mozglue'))

# Assign the function's prototype to get_test_name
libmozglue.GetTestName.argtypes = [ctypes.c_int32]
libmozglue.GetTestName.restype = ctypes.c_char_p

# Global sqlite3 connection
db = sqlite3.connect('/tmp/perfherder.db', check_same_thread=False)
db.row_factory = sqlite3.Row

# Global thread lock to protect the database
db_lock = threading.Lock()

def get_test_name(test_id):
    """
    Given a test_id, return its test_
