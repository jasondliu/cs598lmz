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

def test_callback_registered():
    sqlite3.threadsafety = 1
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb)
    sqlite3.connect(DB_URI, uri=True)
    del my_threading_local.a

test_callback_registered()
</code>
Edit:
I've updated the code to match the changes since I last ran it. I'm using <code>sqlite3.enable_callback_tracebacks(True)</code> and I've removed the <code>ctypes.c_void_p</code> things.


A:

This is not a bug.
Per the documentation:
<blockquote>
<p>By default, the sqlite3 module opens transactions implicitly before a Data Modification Language (DML) statement (i.e. <code>&lt;code&gt;INSERT&lt;/code&gt;</code>, <code>&lt;code&gt;UPDATE&lt;/code&gt;</code> or <code>&lt;
