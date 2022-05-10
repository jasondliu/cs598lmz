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

def test_callback():
    try:
        del my_threading_local.a
    except AttributeError:
        pass

    cb = sqlite3.SQLiteCallback(my_cb)
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'), use_errno=True)
    lib.sqlite3_shutdown()
    lib.sqlite3_config(ctypes.c_int(1), cb)
    lib.sqlite3_initialize()
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    try:
        conn.execute("select test(1, 2)").fetchall()
        assert my_threading_local.a
    finally:
        conn.close()
        lib.sqlite3_shutdown()
