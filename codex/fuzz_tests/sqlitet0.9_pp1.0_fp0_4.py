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

snprintf = ctypes.CDLL(None).snprintf
snprintf.restype = ctypes.c_int
snprintf.argtypes = [ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p]

libsqlite = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
libsqlite.sqlite3_shutdown.argtypes = ctypes.c_void_p
libsqlite.sqlite3_config.argtypes = [ctypes.c_int, ctypes.c_void_p]
libsqlite.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
libsqlite.sqlite3_open.restype = ctypes.c_int

def main():
    for i in range(1000):
        p = ctypes.c_void_p(0)
        libsqlite.sqlite3_config(19, None)
        libsqlite.sqlite
