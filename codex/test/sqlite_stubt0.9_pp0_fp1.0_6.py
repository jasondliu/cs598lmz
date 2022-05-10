import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION = 201

try:
    sqlite3.enable_load_extension(True)
except AttributeError:
    pass

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
lib.sqlite3_create_function.argtypes = [ctypes.c_int, ctypes.c_char_p,
    ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
lib.sqlite3_create_function.restype = ctypes.c_int

lib.sqlite3_enable_load_extension.argtypes = [ctypes.c_int, ctypes.c_int]
lib.sqlite3_enable_load_extension.restype = ctypes.c_int

