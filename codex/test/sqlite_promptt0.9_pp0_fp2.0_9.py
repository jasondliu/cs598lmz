import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() in multi-thread
conn = sqlite3.connect('test_thread.db')
