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


def test_called_from_sqlite3_open_v2():
    my_cb_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    libc = ctypes.util.find_library('c')
    libsqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
    sqlite3_open_v2 = libsqlite3.sqlite3_open_v2
    sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]

    a = ctypes.c_void_p()

    assert libc.getenv("PYTHON_SQLITE3_MEMORY_OPEN_CALLBACK") == "1"

