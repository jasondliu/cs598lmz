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

def test_cb(p):
    a = my_threading_local.a
    a.execute("SELECT test(?, ?)", (1, 2))
    return 1

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_config(1, 1)

    db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    db.create_function("my_cb", 0, my_cb)
    db.create_function("test_cb", 0, test_cb)

    db.execute("SELECT my_cb()")
    db.execute("SELECT test_cb()")

if __name__ == "__main__":
    main()
