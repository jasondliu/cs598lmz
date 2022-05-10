import ctypes
import ctypes.util
import threading
import sqlite3
import os

class CDLL(ctypes.CDLL):
    def __init__(self, name, mode=ctypes.RTLD_GLOBAL, handle=None,
                 use_errno=False, use_last_error=False):
        super(CDLL, self).__init__(name, mode, handle, use_errno, use_last_error)

        # int dlclose(void *handle);
        self._dlclose = self._dlopen = self['dlclose']
        self._dlclose.argtypes = [ctypes.c_void_p]
        self._dlclose.restype = ctypes.c_int

        # void *dlopen(const char *filename, int flag);
        self._dlopen = self['dlopen']
        self._dlopen.argtypes = [ctypes.c_char_p, ctypes.c_int]
        self._dlopen.restype = ctypes.c_void_p

    def __del__(self):
        if self._handle:
            self._dlclose(self._handle)

