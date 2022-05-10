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

sqlite3.sqlite3_set_authorizer(my_cb, None)
</code>
<code>test.py</code>
<code>import _test

def test():
    with my_threading_local.a:
        connection = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        cursor = connection.cursor()
        print(list(cursor.execute("SELECT test(1, 2)")))
</code>
To reproduce the leak just call <code>test</code> multiple times. 
I have found the <code>my_cb</code> function and many functions in <code>libsqlite3</code> that are never released in the cpython code.
I assume this is a bug in cpython and python should not be used in production until it is fixed. 
Calling <code>gc.disable()</code> before running <code>test</code> does not help.

