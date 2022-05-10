import ctypes
import ctypes.util
import threading
import sqlite3

from . import _lib

_lib.lib.sqlite3_enable_load_extension.restype = ctypes.c_int
_lib.lib.sqlite3_enable_load_extension.argtypes = [ctypes.c_void_p, ctypes.c_int]

_lib.lib.sqlite3_load_extension.restype = ctypes.c_int
_lib.lib.sqlite3_load_extension.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p)]

_lib.lib.sqlite3_extended_result_codes.restype = ctypes.c_int
_lib.lib.sqlite3_extended_result_codes.argtypes = [ctypes.c_void_p, ctypes.c_int]

_lib.lib.sqlite3_initialize.restype = ctypes.c_int
_lib.lib.sqlite3_initial
