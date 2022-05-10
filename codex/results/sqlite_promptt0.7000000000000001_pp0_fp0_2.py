import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/xiang/ssd/data/test.db",check_same_thread=False)

def get_driver():
    # locate the library
    _libc = ctypes.util.find_library("c")
    _libc = ctypes.CDLL(_libc, use_errno=True)
    libc = ctypes.CDLL("libc.so.6", use_errno=True)

    # set up lock
    # libc.pthread_mutex_lock.argtypes = [ctypes.POINTER(ctypes.c_int)]
    # libc.pthread_mutex_lock.restype = ctypes.c_int

    # libc.pthread_mutex_unlock.argtypes = [ctypes.POINTER(ctypes.c_int)]
    # libc.pthread_mutex_unlock.restype = ctypes.c_int

    # lock = ctypes.c_int()

    # def _lock():
    #     if libc.pthread_mutex_lock(ctypes.
