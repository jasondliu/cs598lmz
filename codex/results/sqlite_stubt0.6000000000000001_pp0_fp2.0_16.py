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

    assert a.execute("SELECT test(1, 1)").fetchone()[0] == 1
    return 0

def my_cb3(p):
    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.optimize_tracebacks(True)

    sqlite3.enable_shared_cache(True)

    print(ctypes.util.find_library("sqlite3"))

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    lib.sqlite3_config(1, 1)

    lib.sqlite3_config(6, 1)

    lib.sqlite3_config(7, 1)

    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    c.enable_load_extension(True)

    c.load_extension("sqlite3-pythonsqlite")

   
