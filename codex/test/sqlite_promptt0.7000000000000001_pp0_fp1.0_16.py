import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("dbname='%s'" % (dbname))

def set_debug(debug):
    global __DEBUG__
    __DEBUG__ = debug

