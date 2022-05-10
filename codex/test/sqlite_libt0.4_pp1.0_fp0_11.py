import ctypes
import ctypes.util
import threading
import sqlite3
import time

__all__ = ['get_backtrace', 'get_backtrace_symbols', 'get_backtrace_symbols_fd', 'get_backtrace_symbols_fd_name']

_libc = ctypes.CDLL(ctypes.util.find_library('c'))

_libc.backtrace.restype = ctypes.c_int
_libc.backtrace.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_int]

_libc.backtrace_symbols.restype = ctypes.POINTER(ctypes.c_char_p)
_libc.backtrace_symbols.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_int]

_libc.backtrace_symbols_fd.restype = ctypes.c_int
