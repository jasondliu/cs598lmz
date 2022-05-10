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

sqlite3.sqlite3_open_v2(DB_URI.encode('utf-8'), ctypes.byref(my_threading_local.db), 0x00000003, ctypes.c_char_p(0))
sqlite3.sqlite3_create_function(my_threading_local.db, b"my_cb", 0, 1, 0, my_cb, 0, 0)

my_threading_local.db.contents.pVfs = 0

my_threading_local.a.execute("select my_cb()")
my_threading_local.a.execute("select test(1, 2)")

