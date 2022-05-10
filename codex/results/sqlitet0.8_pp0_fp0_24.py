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

# Define the SQLite callback function
sqlite3.sqlite3_progress_handler = sqlite3.sqlite_api.sqlite3_progress_handler
sqlite3.sqlite3_progress_handler(ctypes.c_void_p(0), 1000,
                                 sqlite3.sqlite3_api.sqlite3_progress_handler_py(my_cb))

# Try to create a table, which will cause the callback to run
a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.execute("create table a (ii integer, jj integer);")

# If the callback code does not call Py_XIncref, then after the create table
# operation, the a variable will be inaccessible and will not be finalized
# upon exiting the scope.  This means that the second "select" will fail with
# a segfault (any attempt to access the variable will fail).
print(my_threading_local.a.execute("SELECT test(?, ?)", (1, 2)).fetchall())
</code
