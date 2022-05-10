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
    dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    dll.sqlite3_config(1, my_cb, None)
    dll.sqlite3_initialize()

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    assert a.execute("SELECT test(1,2)").fetchone()[0] == 1
    assert a.execute("SELECT test(1,2)").fetchone()[0] == 1
    assert a.execute("SELECT test(1,2)").fetchone()[0] == 1

    assert my_threading_local.a.execute("SELECT test(1,2)").fetchone()[0] == 1
    assert my_threading_local.a.execute("SELECT test(1,2)").fetchone()[0] == 1
    assert my_threading_local.a.execute("SELECT test(1,2)").fetchone()[0] == 1

    a
