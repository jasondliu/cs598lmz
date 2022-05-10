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

lib = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
lib.my_cb.argtypes = [ctypes.c_void_p]
lib.my_cb.restype = ctypes.c_int

with sqlite3.connect(DB_URI, uri=True) as root_conn:
    root_conn.enable_load_extension(True)
    root_conn.load_extension("pysqlite_ext")
    ptr = root_conn.connection.create_function("my_cb", 1, my_cb)

    my_threading_local.a = None

    lib.my_cb(ptr)

    cursor = my_threading_local.a.cursor()
    cursor.execute("SELECT test(?, ?)", [1, 2])

    del my_threading_local.a
    my_threading_local.a = None

    del cursor
    root_conn.connection.delete_function("my_cb")
