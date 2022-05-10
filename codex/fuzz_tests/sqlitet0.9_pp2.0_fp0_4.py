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

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
lib.sqlite3_aggregate_context.restype = ctypes.c_void_p

ret = lib.sqlite3_initialize()
assert ret == 0

conn_ptr = ctypes.c_void_p()

ret = lib.sqlite3_open(ctypes.c_char_p(DB_URI.encode("utf-8")), ctypes.byref(conn_ptr))

assert ret == 0
conn = ctypes.cast(conn_ptr, ctypes.py_object).value

assert isinstance(conn, sqlite3.Connection)

ret = conn.create_function("test", 1, my_cb)
assert ret is None

c = conn.cursor()
c.execute("SELECT test(1)")

my_cb(None)
a = my_threading_local.a

assert len(c.description) == 1

c.close()
conn.close()
