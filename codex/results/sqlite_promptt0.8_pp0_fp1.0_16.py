import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() with timeout when another thread is holding a connection
# with the same connection filename

libc = ctypes.CDLL(ctypes.util.find_library('c'))
pthread_mutex_t = ctypes.POINTER(ctypes.c_int)
pthread_mutex_lock = libc.pthread_mutex_lock
pthread_mutex_lock.argtypes = [pthread_mutex_t]
pthread_mutex_lock.restype = ctypes.c_int

pthread_mutex_unlock = libc.pthread_mutex_unlock
pthread_mutex_unlock.argtypes = [pthread_mutex_t]
pthread_mutex_unlock.restype = ctypes.c_int

lock = ctypes.c_int()
l = pthread_mutex_t.from_address(ctypes.addressof(lock))

def other_thread():
    with sqlite3.connect(':memory:') as conn:
        cursor = conn.cursor()
        cursor.execute
