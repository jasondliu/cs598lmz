import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection().set_trace_callback()

db = sqlite3.connect(':memory:')

_sqlite_lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))

@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_char_p)
def sqlite3_trace_callback_func(arg, sql):
    print("trace_callback %r" % (sql,))

_sqlite_lib.sqlite3_trace_v2.argtypes = (ctypes.c_void_p, ctypes.c_int,
                                         ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_char_p),
                                         ctypes.c_void_p)
_sqlite_lib.sqlite3_trace_v2.restype = ctypes.c_int
