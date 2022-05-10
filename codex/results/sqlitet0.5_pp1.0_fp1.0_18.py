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

sqlite3.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.db))
sqlite3.sqlite3_busy_handler(my_threading_local.db, my_cb, None)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

def test_fn(a, b):
    return a

a.create_function("test", 2, test_fn)

my_threading_local.a = a

#
# This function will block until the busy handler is called, and the busy
# handler will call the test_fn function.
#
a.execute("select test(1, 2)")
</code>
This is the output I get from running the above code:
<code>$ python3.6 test.py
Exception ignored in: &lt;bound method deleting_conn.__del__ of &lt;sqlite3.Connection object at 0x7f3f3c6d9550&gt;&gt;
Traceback (
