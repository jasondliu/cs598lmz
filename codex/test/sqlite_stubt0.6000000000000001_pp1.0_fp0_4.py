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

def my_cb_del(p):
    del my_threading_local.a
    return 1

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_test_control.argtypes = [ctypes.c_int, ctypes.c_void_p]
    lib.sqlite3_test_control.restype = ctypes.c_int

    lib.sqlite3_test_control(100, ctypes.cast(ctypes.py_object(my_cb), ctypes.c_void_p))
    lib.sqlite3_test_control(101, ctypes.cast(ctypes.py_object(my_cb_del), ctypes.c_void_p))

if __name__ == '__main__':
    main()
