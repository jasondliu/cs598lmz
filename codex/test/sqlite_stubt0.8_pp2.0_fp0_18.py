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

def main():
    sqlite3.enable_callback_tracebacks(True)
    libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    libsqlite3.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))
    libsqlite3.sqlite3_soft_heap_limit(ctypes.c_int(10 * 1024 * 1024))
    libsqlite3.sqlite3_config(ctypes.c_int(7), my_cb)

    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn2(a, b):
        return a

    c.create_function("test", 2, test_fn2)

    my_threading_local.c = c

    print(my_threading_local.c.execute("SELECT test(?, ?)", (1, 2)).fetchone()[0])

