import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() with multiple threads.

if ctypes.util.find_library('c') == None:
    print('Test fai
