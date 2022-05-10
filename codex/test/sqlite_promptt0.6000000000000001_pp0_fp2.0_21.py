import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() and .execute()

import time

# Declare the global variables
libc = ctypes.CDLL(ctypes.util.find_library('c'))

