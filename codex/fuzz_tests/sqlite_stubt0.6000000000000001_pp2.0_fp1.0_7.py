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

# We need to make sure that the reference to the connection instance is
# not cleared until the test_fn is called.
my_callback_obj = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_test_control(101, my_callback_obj, None)

con = sqlite3.connect(DB_URI, uri=True)
cur = con.cursor()

cur.execute("select test(1, 2)")
cur.fetchall()

del cur
del con

# This should not segfault
lib.sqlite3_test_control(101, my_callback_obj, None)
