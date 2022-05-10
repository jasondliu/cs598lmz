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

def my_main():
    libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
    initialize = libc.sqlite3_initialize
    initialize.argtypes = None
    initialize.restype = ctypes.c_int

    shutdown = libc.sqlite3_shutdown
    shutdown.argtypes = None
    shutdown.restype = ctypes.c_int

    config = libc.sqlite3_config
    config.argtypes = [
        ctypes.c_int, ctypes.c_void_p ]
    config.restype = ctypes.c_int

    open_v2 = libc.sqlite3_open_v2
    open_v2.argtypes = [
        ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int,
        ctypes.c_char_p ]
    open_v2.restype = ctypes.c_int

    close = libc.sqlite3_close_v
