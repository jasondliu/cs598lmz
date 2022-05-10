import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.pthread_key_create.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_void_p]
libc.pthread_key_create.restype = ctypes.c_int
libc.pthread_setspecific.argtypes = [ctypes.c_int, ctypes.c_void_p]
libc.pthread_setspecific.restype = ctypes.c_int
libc.pthread_getspecific.argtypes = [ctypes.c_int]
libc.pthread_getspecific.restype = ctypes.c_void_p

class ThreadLocal(object):
    def __init__(self):
        self.key = ctypes.c_int()
        libc.pthread_key_create(ctypes.byref(self.key), None)

    def get(self):
        return libc.pthread_
