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

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("mylib"))
lib.mylib_p_callback.argtypes = [my_cb]
lib.mylib_p_callback(my_cb)
</code>


A:

You don't need to use the connection object in <code>threading.local()</code> or create a new connection object every time the callback is called.
You can use a global variable, and create the connection object upon the first time of callback call and reuse the connection object.

