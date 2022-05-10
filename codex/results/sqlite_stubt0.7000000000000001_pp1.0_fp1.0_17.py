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

# Load the library
sqlite_lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

sqlite_lib.sqlite3_open(":memory:", ctypes.byref(my_threading_local.conn_ptr))

sqlite_lib.sqlite3_create_function(my_threading_local.conn_ptr, b"my_cb", 0, 1, ctypes.py_object(my_cb), 0, 0)
sqlite_lib.sqlite3_close(my_threading_local.conn_ptr)
</code>
When I run this in Python 3.7.0, the <code>__del__</code> method of the <code>deleting_conn</code> object is never called.
Now, I know that the object is not being garbage collected because of the <code>ctypes</code> reference, but I don't know what to do about it.
When I try to create a <code>__del__</code> method for the <code>ctypes.py_object</code> class,
