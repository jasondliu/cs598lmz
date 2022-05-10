import ctypes
import ctypes.util
import threading
import sqlite3
import io
import mimetypes
import sys


class AtlasClient:
    def __init__(self):
        self.lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('Atlas'))
        self.lib.Atlas_new.restype = ctypes.c_void_p
        self.lib.Atlas_new.argtypes = [ctypes.c_int]

        self.lib.Atlas_set_pin.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]

        self.lib.Atlas_get_log.restype = ctypes.c_char_p
        self.lib.Atlas_get_log.argtypes = [ctypes.c_void_p]

        self.lib.Atlas_get_log_severity.restype = ctypes.c_int
        self.lib.Atlas_get_log_severity.argtypes = [ctypes.c_void_p]
