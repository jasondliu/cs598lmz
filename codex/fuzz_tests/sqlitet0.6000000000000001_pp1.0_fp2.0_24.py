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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_enable_load_extension(None, 1)
lib.sqlite3_load_extension(None, "/tmp/sqlite3_ext/libtest_fn.so", None)

lib.my_cb.restype = ctypes.c_int
lib.my_cb.argtypes = (ctypes.c_void_p,)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.create_function("my_cb", 1, my_cb)

# Ensure that the thread-local connection is created
a.execute("SELECT my_cb(1);")
del a # Delete the connection, but not the thread-local one

# Use the thread-local connection
t = my_threading_local.a.execute("SELECT test(1,2);").fetchall()

assert t[0][0] == 1
</code>
The problem is that once I reach <code>
