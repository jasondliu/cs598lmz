import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
sqlite3.connect("test.db")
sqlite3.connect("test.db", check_same_thread=False)
# Test ctypes.util.find_library
ctypes.util.find_library("c")
# Test threading.Thread
threading.Thread(target=lambda: None)
