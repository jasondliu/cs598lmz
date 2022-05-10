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
    a = my_threading_local.a
    a.execute("select test(1, 2)")
    return 1

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(1, my_cb, None)
lib.sqlite3_config(2, my_cb2, None)

a = sqlite3.connect(DB_URI, uri=True)
a.execute("select 1")
</code>
The above code works fine, but if I remove the <code>a.execute("select 1")</code> line, I get a segfault when the <code>a</code> object is garbage collected.
I've also tried using a <code>sqlite3.Connection</code> object instead of <code>deleting_conn</code> in the callback, but that doesn't work either.
I'm using Python 3.7.3 on macOS 10.14.5.

