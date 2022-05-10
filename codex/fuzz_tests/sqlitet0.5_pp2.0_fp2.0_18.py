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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(ctypes.c_void_p()), 1, None)
sqlite3.sqlite3_set_authorizer(my_threading_local.a.connection.connection, my_cb, None)
</code>
This will crash with the following error:
<code>Fatal Python error: PyEval_RestoreThread: NULL tstate
</code>
If I remove the <code>sqlite3.sqlite3_set_authorizer</code> line, it will run without error. Why is this happening?
I am using Python 3.4.3 and SQLite 3.8.8.1.


A:

The problem is that you are calling <code>sqlite3_set_authorizer()</code> from inside a callback. That is not allowed.
The documentation for <code>sqlite3_set_authorizer()</code> says:
<blockquote>
<p>Applications should invoke <code>&lt;code&gt;sqlite3_set_authorizer
