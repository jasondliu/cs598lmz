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

def test_function():
    dll = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    dll.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.db))
    dll.sqlite3_create_function(
        my_threading_local.db,
        b"test",
        2,
        ctypes.cast(
            ctypes.pythonapi.PyCapsule_New.restype(
                ctypes.py_object, ctypes.c_void_p),
            ctypes.c_void_p),
        b"test_fn",
        None)
    dll.sqlite3_close(my_threading_local.db)

def main():
    for i in range(0, 100):
        t = threading.Thread(target=test_function)
        t.start()
        t.join()

main()
