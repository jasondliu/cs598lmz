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

def test_a():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.create_function("init", 0, my_cb)

def test_b():
    threading.local().a.execute("select test(1, 2);")

def main(int=None):
    dll = ctypes.util.find_library("sqlite3")
    if dll is None:
        raise RuntimeError("Could not find SQLite3 library")

    # Initialize the library; this will be called automatically before use
    # if this is not done.
    sqlite3.load_extension(d
