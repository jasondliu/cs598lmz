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
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    libc.pthread_create.argtypes = [ctypes.POINTER(ctypes.c_void_p),
                                    ctypes.c_void_p,
                                    ctypes.c_void_p,
                                    ctypes.c_void_p]
    libc.pthread_create.restype = ctypes.c_int

    p = ctypes.c_void_p()
    libc.pthread_create(ctypes.byref(p), None, my_cb, None)
    libc.pthread_join(p, None)

    a = my_threading_local.a
    assert a.execute("select test(1, 2)").fetchone()[0] == 1

if __name__ == '__main__':
    test_function()
