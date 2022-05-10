import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() as a context manager

libsqlite = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

