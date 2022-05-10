import ctypes
import ctypes.util
import threading
import sqlite3
import json
import os

class Server:
    def __init__(self, port=12345, db=None, dbargs=(),
                 fileno=None, own_socket=False, auto_start=False):
        self.port = port
        self.db = db
        self.dbargs = dbargs
        self.fileno = fileno
        self.is_own_socket = own_socket
        self.auto_start = auto_start
        self.running = False
        self.thread = None

        c_char_p = ctypes.POINTER(ctypes.c_char)
        self._lib = None
        self._openfd = None
        self._getfd = None
        self._clifd = None
        self._recv = None
        self._send = None
        self._close = None
        self._shutdown = None
        self._recv.argtypes = [ctypes.c_int, c_char_p, ctypes.c_int]
        self._recv.restype = ctypes.c_int
        self
