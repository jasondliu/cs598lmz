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

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('libsqlite3.so'))
lib.sqlite3_open_v2.restype = None
lib.sqlite3_open_v2.argtypes = (ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)

libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
libc.pthread_self.restype = ctypes.c_long
libc.pthread_create.restype = ctypes.c_int

assert libc.pthread_create(ctypes.c_void_p(), None, ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)(my_cb), None) == 0

handle = ctypes.c_void_p()
ret = lib.sqlite3_open_v2(ctypes.c_char_p(DB_URI), ctypes
