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

def my_cb_init(p):
    return my_cb(p)

def my_cb_shutdown(p):
    return 1

my_cb_init_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb_init)
my_cb_shutdown_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb_shutdown)

sqlite3.sqlite3_initialize()

sqlite3.sqlite3_auto_extension(my_cb_init_func)
sqlite3.sqlite3_shutdown_auto_extension(my_cb_shutdown_func)

conn = sqlite3.connect(DB_URI, uri=True)

cur = conn.cursor()

cur.execute("select test(1, 2)")

print(cur.fetchone())

cur.execute("select test(1, 2)")

print(cur.fetch
