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

c = ctypes.CDLL(ctypes.util.find_library("sqlite3"), ctypes.RTLD_GLOBAL)
c.sqlite3_config(1, ctypes.c_void_p())
c.sqlite3_enable_load_extension(None, 1)
c.sqlite3_auto_extension(ctypes.cast(ctypes.pythonapi.PyCapsule_New.restype(ctypes.c_void_p)(my_cb, None, None), ctypes.c_void_p))

conn = sqlite3.connect(DB_URI, uri=True)
conn.execute("SELECT load_extension('test')")

print(conn.execute("SELECT test(1, 2)").fetchone()[0])
print(conn.execute("SELECT test(1, 2)").fetchone()[0])
print(conn.execute("SELECT test(1, 2)").fetchone()[0])

print(my_threading_local.a)
