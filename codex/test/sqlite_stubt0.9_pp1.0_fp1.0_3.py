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

my_cb_t = sqlite3.ffi.callback("int(int)", my_cb)

sqlite3.api.sqlite3_opaque_test_config(my_cb_t, ctypes.c_void_p(ctypes.util.find_library("c")))

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.execute("SELECT test(5, 6)").fetchone()

a.execute("CREATE TABLE test(x INTEGER)")

a.execute("INSERT INTO test VALUES (1)")
a.execute("INSERT INTO test VALUES (2)")

# This insert causes the next fetchone call to throw a segfault.
a.execute("INSERT INTO test VALUES (3)")

# Commenting out other threads resolves the segfault below.
my_threading_local.b = True

# It appears I can also attach another DB if I use DB_URI + "2" as the URI.

