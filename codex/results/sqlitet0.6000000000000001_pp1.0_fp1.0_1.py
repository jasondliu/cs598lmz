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

def my_cb_err(p):
    def test_fn(a, b):
        return a

    my_threading_local.a.create_function("test", 2, test_fn)

    return 1

def main():
    try:
        import argparse
    except ImportError:
        print("SKIP")
        raise SystemExit

    parser = argparse.ArgumentParser()
    parser.add_argument("--run-err", action='store_true')
    args = parser.parse_args()

    sqlite3.threadsafety = 2

    lib = ctypes.util.find_library('sqlite3')
    if lib is None:
        print('SKIP cannot find sqlite3 library')
        raise SystemExit

    lib = ctypes.CDLL(lib)
    sqlite3_open = lib.sqlite3_open
    sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
    sqlite3_open.restype = ctypes.c
