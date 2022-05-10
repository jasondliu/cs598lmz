import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("xev.db")


Xlib = ctypes.CDLL("libX11.so.6")
X = ctypes.CDLL("libX11.so.6")


