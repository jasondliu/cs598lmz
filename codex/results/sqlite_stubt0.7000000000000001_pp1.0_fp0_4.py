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

def test():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_open(b":memory:", ctypes.byref(ctypes.c_void_p()))
    lib.sqlite3_create_function(
        my_threading_local.a.connection.__enter__()._sqlite_conn,
        b"test", 2, None, ctypes.cast(my_cb, ctypes.c_void_p)
    )

test()
</code>
And the output from a Python 3.6.8 interpreter:
<code>Exception ignored in: &lt;function test at 0x7f4e4c4f4200&gt;
Traceback (most recent call last):
  File "&lt;string&gt;", line 24, in test
  File "&lt;string&gt;", line 18, in my_cb
  File "/usr/lib/python3.6/site-packages/sqlite3/dbapi2.py", line 2463, in create
