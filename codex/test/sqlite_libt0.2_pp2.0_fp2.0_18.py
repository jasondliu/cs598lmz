import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys

class libc:
    def __init__(self):
        self.libc = ctypes.CDLL(ctypes.util.find_library('c'))
        self.libc.sigprocmask.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong)]
        self.libc.sigprocmask.restype = ctypes.c_int
        self.libc.sigemptyset.argtypes = [ctypes.POINTER(ctypes.c_ulong)]
        self.libc.sigemptyset.restype = ctypes.c_int
        self.libc.sigaddset.argtypes = [ctypes.POINTER(ctypes.c_ulong), ctypes.c_int]
        self.libc.sigaddset.restype = ctypes.c_int
