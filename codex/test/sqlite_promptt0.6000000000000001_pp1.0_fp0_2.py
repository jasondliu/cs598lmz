import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:').execute('select 1').fetchall()

from . import _pysqlite_worker
from . import _pysqlite_worker_thread

_libc_name = ctypes.util.find_library('c')
_libc = ctypes.CDLL(_libc_name, use_errno=True)

_THREAD_ONCE_INIT = 0
_thread_once_lock = threading.Lock()

_pthread_once = _libc.pthread_once
_pthread_once.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_void_p]
_pthread_once.restype = ctypes.c_int

_pthread_key_create = _libc.pthread_key_create
_pthread_key_create.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_void_p]
_pthread_key_create.restype = ctypes.c_int
