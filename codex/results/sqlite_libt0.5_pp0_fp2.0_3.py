import ctypes
import ctypes.util
import threading
import sqlite3

from . import constants
from . import errors
from . import utils

# pylint: disable=protected-access

class _Cursor(ctypes.Structure):
    _fields_ = [("pVtab", ctypes.c_void_p)]

class _Vtab(ctypes.Structure):
    _fields_ = [("pModule", ctypes.c_void_p),
                ("nRef", ctypes.c_int),
                ("zErrMsg", ctypes.c_char_p)]

class _Module(ctypes.Structure):
    _fields_ = [("iVersion", ctypes.c_int),
                ("xCreate", ctypes.c_void_p),
                ("xConnect", ctypes.c_void_p),
                ("xBestIndex", ctypes.c_void_p),
                ("xDisconnect", ctypes.c_void_p),
                ("xDestroy", ctypes.c_void_p),
                ("xOpen", ctypes.c_void_p),
                ("xClose", c
