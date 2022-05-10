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

def sqlite3_open_v2(filename, mode, vfs):
    return sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

ctypes.CDLL(ctypes.util.find_library("sqlite3"), mode=ctypes.RTLD_GLOBAL)

libsqlite3 = ctypes.CDLL("libsqlite3.so.0")
libsqlite3.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_char_p]
libsqlite3.sqlite3_open_v2.restype = ctypes.c_int
libsqlite3.sqlite3_open_v2.errcheck = lambda result, func, arguments: sqlite3_open_v2(*arguments)

libsqlite3.sqlite3_enable_load_extension(my_threading_local.a.connection, 1)
