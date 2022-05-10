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

p = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
libsqlite3.sqlite3_thread_cleanup(p)
</code>
Now, it turns out that if you run this on its own, it works fine. However, if you run it as part of a set of tests (I'm using pytest), you get a segfault.
I've tracked the problem down to the following code:
<code>import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading
