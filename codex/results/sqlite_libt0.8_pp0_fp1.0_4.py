import ctypes
import ctypes.util
import threading
import sqlite3
import os
import hashlib
import tempfile

if os.name == 'nt':
    SOCKET = ctypes.c_uint64
else:
    SOCKET = ctypes.c_int64


class _conn_info(ctypes.Structure):
    _fields_ = [("socket", SOCKET),
                ("timestamp", ctypes.c_int64),
                ("file", ctypes.c_char_p),
                ("file_size", ctypes.c_int64),
                ("file_md5", ctypes.c_char*33)]


_tmp_dir = tempfile.mkdtemp()

_libc = ctypes.CDLL(ctypes.util.find_library("c"))
_libc.connect_log_init.restype = ctypes.c_void_p
_libc.connect_log_add.argtypes = (ctypes.c_void_p, _conn_info, ctypes.c_size_t)
_libc.connect_log_add.restype = ctypes.c_int
