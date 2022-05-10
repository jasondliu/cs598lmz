import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

con = sqlite3.connect(':memory:')
