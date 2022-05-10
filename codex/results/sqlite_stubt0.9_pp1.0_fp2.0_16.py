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

def my_cb_trace(a, b):
    return 1

l = sqlite3.load_extension(ctypes.util.find_library("sqlite3"), "/usr/local/lib/libsqlite3functions.dylib")
sqlite3.create_function("test", 2, l)
sqlite3.connect(":memory:")
my_conn.set_authorizer(my_cb)
my_conn.execute("select test(3, 4)")
del my_threading_local.a
# this is safe
my_conn.execute("select test(3, 4)")

sqlite3.trace(my_conn.cursor(), my_cb_trace)
my_conn.execute("select test(3, 4)")
del my_threading_local.a
# this is not
my_conn.execute("select test(3, 4)")
</code>
I know that these things aren't quite the same as deleting <code>a</code> but surely it can't be a coincidence that the unintended side effect only happens when using the same thread.
