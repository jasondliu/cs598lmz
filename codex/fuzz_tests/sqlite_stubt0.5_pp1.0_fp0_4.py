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
lib.sqlite3_config(1)
lib.sqlite3_config(7, my_cb, None)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.execute("select test(1, 2)")
</code>
I'm using <code>deleting_conn</code> to ensure the <code>sqlite3.Connection</code> instance gets deleted.
The problem is that I'm getting a segfault.
If I comment out the line <code>my_threading_local.a = a</code>, the segfault goes away.
If I change <code>my_threading_local</code> to be a global, the segfault goes away.
I don't understand why the segfault happens.
I'm using Python 3.5.3 on Ubuntu 16.04.

