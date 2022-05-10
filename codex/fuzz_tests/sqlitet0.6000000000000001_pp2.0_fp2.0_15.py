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

def test_init_once():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.create_function("test", 2, lambda a, b: a)
    a.close()

    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_shutdown()

    lib.sqlite3_initialize()
    lib.sqlite3_config(ctypes.c_int(1), my_cb, None)

    b = sqlite3.connect(DB_URI, uri=True)
    b.execute("select test(5, 6)")

    c = my_threading_local.a

    c.execute("select test(5, 6)")

    lib.sqlite3_shutdown()
    lib.sqlite3_initialize()

if __name__ == "__main__":
    test_init_once()
