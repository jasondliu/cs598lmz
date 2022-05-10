import ctypes
import ctypes.util
import threading
import sqlite3
import atexit

class Music:
    _lib = ctypes.util.find_library('mpg123')
    if not _lib:
        raise ImportError("There is no mpg123 library available.")
    _lib = ctypes.CDLL(_lib)

    _mh = _lib.mpg123_new(None, None)
    _lib.mpg123_open_feed(_mh)
    _lib.mpg123_getformat(_mh, ctypes.byref(ctypes.c_long()),
                          ctypes.byref(ctypes.c_int()), ctypes.byref(ctypes.c_int()))

    def __init__(self):
        self._buffer = ctypes.create_string_buffer(10240)
        self.library = sqlite3.connect("music.db", check_same_thread=False)
        self.c = self.library.cursor()

