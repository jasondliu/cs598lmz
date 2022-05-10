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
    # Load the library.
    sqlite_dll = ctypes.util.find_library('sqlite3')
    if not sqlite_dll:
        raise Exception("unable to locate sqlite dll")

    sqlite_dll = ctypes.CDLL(sqlite_dll)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    class ptr(ctypes.Structure):
        _fields_ = [
                ("a", ctypes.c_void_p),
                ("b", ctypes.c_void_p),
                ("c", ctypes.c_void_p),
                ("d", ctypes.c_void_p),
                ("e", ctypes.c_void_p),
                ("f", ctypes.c_void_p),
                ("g", ctypes.c_void_p),
                ]
    p = ctypes.pointer(ptr(0,0,0,0,0,0,0))
    b =
