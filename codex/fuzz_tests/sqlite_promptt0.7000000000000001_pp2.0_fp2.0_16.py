import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
db = sqlite3.connect(':memory:')

# Instantiate ctypes.PyDLL()
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Define C-function to acquire lock
libc.pthread_mutex_trylock.argtypes = [ctypes.c_void_p]
libc.pthread_mutex_trylock.restype  = ctypes.c_int

# Define C-function to release lock
libc.pthread_mutex_unlock.argtypes  = [ctypes.c_void_p]
libc.pthread_mutex_unlock.restype   = None

# Set db.connection.isolation_level = None
db.isolation_level = None

# Acquire lock on db.connection
lock = db.execute('PRAGMA locking_mode = EXCLUSIVE').fetchall()[0][0]
while libc.pthread_mutex_trylock(lock):
    pass

# Release lock on db.connection
libc
