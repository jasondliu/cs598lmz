import ctypes
import ctypes.util
import threading
import sqlite3

from . import lmdb_cffi

_ffi = ctypes.FFI()

