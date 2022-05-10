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

if __name__ == '__main__':
    ctypes.CDLL(self.dll_name)
    try:
        from sqlite import _sqlite
    except ImportError:
        _sqlite = ctypes.CDLL(ctypes.util.find_library('_sqlite3'))
    _sqlite._sqlite_custom_func_handler.argtypes = [ctypes.py_object, ctypes.py_object]
    _sqlite._sqlite_custom_func_handler.restype = ctypes.c_int
    _sqlite._sqlite_custom_func_handler(my_cb, 0)
