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

_sqlite = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
_sqlite.test.argtypes = [ctypes.c_void_p]
_sqlite.test.restype = ctypes.c_int
_dll = ctypes.CDLL(ctypes.util.find_library("dl"))
_handle = ctypes.c_void_p()
_dll.dlopen(ctypes.c_char_p(b"libpython3.7m.so"), ctypes.c_int(2))
_test_fn = ctypes.c_void_p(_dll.dlsym(_handle, ctypes.c_char_p(b"test_fn")))

_sqlite.test.restype = ctypes.c_int
_sqlite.test.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

_sqlitethread = ctypes.CDLL(ctypes.util.find_library("sqlite3thread"))

_sqlitethread.sqlite3thread
