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
    my_threading_local.a.close()

    return 1

libc = ctypes.CDLL(ctypes.util.find_library("c"))
my_cb_pointer = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
my_cb2_pointer = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb2)

sqlite3.set_hook(my_cb_pointer, None)

#sqlite3.connect(DB_URI, uri=True)
conn = sqlite3.connect(DB_URI, uri=True)
cur = conn.cursor()
cur.execute("select test(1, 2)")

sqlite3.set_hook(my_cb2_pointer, None)

