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

libsqlite3 = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
libsqlite3.sqlite3_progress_handler(my_threading_local.a._handle, 1, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(my_cb))
</code>
The line <code>my_threading_local.a._handle</code> gives me the following error:
<code>AttributeError: 'Connection' object has no attribute '_handle'
</code>
But obviously there is a <code>_handle</code> attribute since a <code>print(dir(obj))</code> shows me <code>_handle</code> as part of the objects attributes.
Any idea how to get this done?


A:

So I managed to call the sqlite3_progress_handler function with:
<code>libsqlite3.sqlite3_progress_handler(my_threading_local.a._sqlite3_connection.connection._handle, 1, ctypes.CFUNCTYPE
