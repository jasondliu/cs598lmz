import ctypes
import ctypes.util
import threading
import sqlite3
import zlib
import os

_mutex = ctypes.CDLL(ctypes.util.find_library('pthread'))
_mutex.pthread_mutex_init.argtypes = [ctypes.POINTER(ctypes.c_ulonglong)]
_mutex.pthread_mutex_init.restype = ctypes.c_int
_mutex.pthread_mutex_lock.argtypes = [ctypes.POINTER(ctypes.c_ulonglong)]
_mutex.pthread_mutex_lock.restype = ctypes.c_int
_mutex.pthread_mutex_unlock.argtypes = [ctypes.POINTER(ctypes.c_ulonglong)]
_mutex.pthread_mutex_unlock.restype = ctypes.c_int

class Mutex:

    def __init__(self):
        self.mutex = ctypes.c_ulonglong(0)

        ret = _mutex.pthread_mutex_init(self.mutex)
        if ret !=
