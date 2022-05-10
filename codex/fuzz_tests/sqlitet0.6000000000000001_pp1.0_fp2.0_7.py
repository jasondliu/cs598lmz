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

def test_conn_is_deleted_when_thread_exits():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_thread_cleanup.restype = ctypes.c_int
    lib.sqlite3_thread_cleanup.argtypes = []
    lib.sqlite3_thread_cleanup()

    lib.sqlite3_thread_init.restype = ctypes.c_int
    lib.sqlite3_thread_init.argtypes = [ctypes.c_char_p]
    lib.sqlite3_thread_init(my_cb)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    b = my_threading_local.a
    assert a.execute("select test(1, 2)").fetchone()[0] == 1
    lib.sqlite3_thread_cleanup()
    del b
    del a
