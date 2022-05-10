import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')
# http://docs.python.org/library/sqlite3.html

class TestSharedCache(object):
    def setup_method(self, method):
        self.libc = ctypes.CDLL(ctypes.util.find_library('c'))
        self.libc.pthread_key_create = self.libc.pthread_key_create
        self.libc.pthread_key_create.argtypes = [ctypes.POINTER(ctypes.c_int),
                                                 ctypes.c_void_p]
        self.libc.pthread_key_create.restype = ctypes.c_int
        self.libc.pthread_setspecific = self.libc.pthread_setspecific
        self.libc.pthread_setspecific.argtypes = [ctypes.c_int, ctypes.c_void_p]
        self.libc.pthread_setspecific.restype = ctypes.c_int
        self.libc.p
