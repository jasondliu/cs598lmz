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

def my_cb2(p):
    a = my_threading_local.a
    a.execute("SELECT test(1, 2)")
    return 1

def my_cb3(p):
    my_threading_local.a.close()
    return 1

def main():
    # check that sqlite3 is compiled with threading support
    libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
    if not hasattr(libc, 'pthread_create'):
        print('sqlite3 is not compiled with threading support')
        return

    lib = ctypes.CDLL("./libsqlitefunctions.so")

    lib.register_callback(my_cb, 0)
    lib.register_callback(my_cb2, 1)
    lib.register_callback(my_cb3, 2)

    conn = sqlite3.connect(DB_URI, uri=True)
    cur = conn.cursor()
