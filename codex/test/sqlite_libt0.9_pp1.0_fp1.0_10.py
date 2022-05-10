import ctypes
import ctypes.util
import threading
import sqlite3
from . import *
from .utils import *

_libtacacs = load_library("tacacs", "tac_authenticate")

_libtacacs.tac_auth_close.argtypes = []
_libtacacs.tac_auth_close.restype = None
_libtacacs.tac_auth_init.argtypes = [ctypes.c_char_p, ctypes.c_char_p,
        ctypes.c_uint]
_libtacacs.tac_auth_init.restype = ctypes.c_void_p
_libtacacs.tac_auth_part.argtypes = [ctypes.c_char_p,
        ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p]
_libtacacs.tac_auth_part.restype = ctypes.c_void_p
