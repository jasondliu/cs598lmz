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

def my_cb_close(p):
    if hasattr(my_threading_local, 'a'):
        my_threading_local.a.close()

    return 1

def main():
    libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    conn_ptr = ctypes.c_void_p(libsqlite3.sqlite3_open_v2(DB_URI,
                                ctypes.pointer(ctypes.c_void_p()),
                                0x00000008,
                                None))
    conn = ctypes.pythonapi.PyCapsule_New(conn_ptr, None, None)
    if not conn:
        raise RuntimeError("PyCapsule_New() failed")

    libsqlite3.sqlite3_set_authorizer(conn_ptr,
                                      ctypes.pythonapi.PyCFunction_New(ctypes.py_object(my_cb),
                                                                       None),
                                      None)

    libsqlite3.sqlite3_
