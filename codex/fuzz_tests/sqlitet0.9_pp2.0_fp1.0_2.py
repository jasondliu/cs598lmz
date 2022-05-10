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


def test_new_db():
    a = my_threading_local.a
    assert a.execute("SELECT test(123, 234)").fetchone()[0] == 123


def main():
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    test_new_db()
    print("hello world")
    libc.exit(0)

main()
