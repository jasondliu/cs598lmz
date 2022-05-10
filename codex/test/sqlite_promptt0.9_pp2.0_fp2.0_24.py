import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:') and sqlite3.connect(':memory:',)
# and fails of threading
