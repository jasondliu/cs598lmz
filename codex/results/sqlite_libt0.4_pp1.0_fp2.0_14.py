import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys

import common

_libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

_libc.signal.argtypes = [ctypes.c_int, ctypes.c_void_p]
_libc.signal.restype = ctypes.c_void_p

_libc.sigaction.argtypes = [ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
_libc.sigaction.restype = ctypes.c_int

_libc.sigemptyset.argtypes = [ctypes.c_void_p]
_libc.sigemptyset.restype = ctypes.c_int

_libc.sigaddset.argtypes = [ctypes.c_void_p, ctypes.c_int]
_libc.sigaddset.restype = ctypes.c_int

_libc.sigprocmask.argtypes =
