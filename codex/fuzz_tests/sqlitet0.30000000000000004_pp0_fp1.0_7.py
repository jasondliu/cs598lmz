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

def my_cb_del(p):
    del my_threading_local.a
    return 1

def test_threading():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_set_authorizer(None, my_cb, my_cb_del)
    lib.sqlite3_enable_load_extension(None, 1)
    lib.sqlite3_load_extension(None, "./test.so", "test_fn", None)
    lib.sqlite3_enable_load_extension(None, 0)
    lib.sqlite3_set_authorizer(None, None, None)

    conn = sqlite3.connect(DB_URI, uri=True)
    cur = conn.cursor()
    cur.execute("select test(1, 2)")
    cur.close()
    conn.close()

threads = []
for i in range(10):
    t = threading.Thread(target=test_threading)
    threads.
