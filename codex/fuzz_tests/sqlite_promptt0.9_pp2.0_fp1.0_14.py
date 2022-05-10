import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(party='*')
# Search directory for dll:
DLL_NAME = ctypes.util.find_library('sqlite3')
if DLL_NAME is None:
    raise Exception("Can't find sqlite3 DLL")
# Load DLL and symbols
sqlite3 = ctypes.cdll.LoadLibrary(DLL_NAME)
sqlite3.sqlite3_open.argtypes = [ctypes.c_char_p,
                                 ctypes.POINTER(ctypes.c_void_p)]
sqlite3.sqlite3_open.restype = ctypes.c_int
sqlite3.sqlite3_prepare_v2.argtypes = [ctypes.c_void_p, ctypes.c_char_p,
                                       ctypes.c_int,
                                       ctypes.POINTER(ctypes.c_void_p),
                                       ctypes.POINTER(ctypes.c_char_p)]
sqlite3.sqlite3_prepare_v2.restype = ctypes.c_int
sqlite3.
