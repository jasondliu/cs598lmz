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
    print(my_threading_local.a.execute("select test(1, 2);").fetchone()[0])

def my_cb3(p):
    print(my_threading_local.a.execute("select test(3, 4);").fetchone()[0])

if __name__ == "__main__":
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    lib.sqlite3_config(1, 1)

    cb1 = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
    cb2 = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb2)
    cb3 = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb3)

    lib.sqlite3_initialize()
    lib.sqlite3_thread_cleanup()

    lib.sqlite3_config(2, cb1, 1)
    lib.
