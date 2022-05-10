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

test = ctypes.cdll.LoadLibrary(ctypes.util.find_library('test'))
test.test_fn.argtypes = [ctypes.c_int]
test.test_fn.restype = ctypes.c_int

test.test_fn(my_cb)
</code>
I've created a C library that calls a Python callback that creates an SQLite connection and registers a user-defined function. The callback returns 1, which is passed back to the C library.
The problem is that when I run this code, I get the following error:
<code>Exception ignored in: &lt;bound method Connection.__del__ of &lt;sqlite3.Connection [closed] object at 0x7f7c8c0e2f30&gt;&gt;
Traceback (most recent call last):
  File "/usr/lib/python3.4/sqlite3/__init__.py", line 593, in __del__
  File "/usr/lib/python3.4/sqlite3/__init__.py", line 589, in close
sql
