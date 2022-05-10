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

sqlite3.sqlite3_initialize()
lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
lib.sqlite3_enable_load_extension(ctypes.c_int(1))
lib.sqlite3_auto_extension(my_cb)

b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
b.execute("select load_extension('')")
b.execute("select test(1, 2)")
b.close()

print "done"
