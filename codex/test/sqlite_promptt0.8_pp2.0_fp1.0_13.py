import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect without the threading.Lock() call
conn = sqlite3.connect('examples.db')
