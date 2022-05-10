import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

libc = ctypes.CDLL(ctypes.util.find_library('c'))

libc.fork.restype = ctypes.c_int
libc.fork.argtypes = []

def fork():
    return libc.fork()

# Test threading.active_count()

def active_count():
    return threading.active_count()

# Test sqlite3.connect()

def connect():
    return sqlite3.connect(':memory:')

# Test sqlite3.connect()

def connect_2():
    return sqlite3.connect(':memory:')

# Test sqlite3.connect()

def connect_3():
    return sqlite3.connect(':memory:')

# Test sqlite3.connect()

def connect_4():
    return sqlite3.connect(':memory:')

# Test sqlite3.connect()

def connect_5():
    return sqlite3.connect(':memory:')

# Test sqlite3.connect()

def connect_6
