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

def my_cb2():
    del my_threading_local.a

    return 1

def test_threading_local():
    """
    Test that a threading local connection is closed when the thread exits.

    This test is only meant to be run on platforms where
    sqlite3_threadsafe() returns 2.
    """
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    assert lib.sqlite3_threadsafe() == 2

    lib.sqlite3_enable_shared_cache(1)

    lib.sqlite3_config(5, my_cb, my_cb2)

    for i in range(5):
        t = threading.Thread(target=lambda: sqlite3.connect(DB_URI))
        t.start()
        t.join()

if __name__ == "__main__":
    test_threading_local()
