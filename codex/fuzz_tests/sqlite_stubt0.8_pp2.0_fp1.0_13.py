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

my_cb(ctypes.c_void_p())
</code>
When I run the code, I see the following error:
<code>sqlite3._sqlite3.OperationalError: unable to open database file
</code>
The error occurs within <code>sqlite3.check_thread_safety()</code>. It seems like the reference to the <code>sqlite3.Connection</code> object is being cleared by the time the check takes place.
Any ideas on how to work around this? Thanks!

