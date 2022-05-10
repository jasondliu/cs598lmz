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

def my_cb2(a, b, c):
    my_threading_local.a.execute("select test(1, 2)")

    return 1

def main():
    src = b"""
    int test1(int p) {
        return p + 1;
    }

    int test2(int x, int y) {
        return x + y;
    }
    """

    my_lib = ctypes.CDLL(None)
    my_lib.test1.argtypes = [ctypes.c_int]
    my_lib.test1.restype = ctypes.c_int
    my_lib.test2.argtypes = [ctypes.c_int, ctypes.c_int]
    my_lib.test2.restype = ctypes.c_int

    sqlite3.enable_callback_tracebacks(True)
    sqlite3._sqlite.load_extension(my_lib, "test1", my_cb)
