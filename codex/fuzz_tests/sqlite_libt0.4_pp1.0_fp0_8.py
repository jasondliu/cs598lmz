import ctypes
import ctypes.util
import threading
import sqlite3

from . import _libc
from . import _util

_libc.load()

_libc.malloc.argtypes = [ctypes.c_size_t]
_libc.malloc.restype = ctypes.c_void_p

_libc.free.argtypes = [ctypes.c_void_p]
_libc.free.restype = None

_libc.realloc.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
_libc.realloc.restype = ctypes.c_void_p

_libc.memset.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_size_t]
_libc.memset.restype = ctypes.c_void_p

_libc.memcpy.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
_libc.memcpy.restype =
