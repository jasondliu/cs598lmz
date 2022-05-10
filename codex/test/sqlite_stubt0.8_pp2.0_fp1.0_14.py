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

def my_cb_factory(p):
    return my_cb

class my_broker:
    def __init__(self):
        self.id_counter = 0

    def __call__(self, n):
        self.id_counter += 1
        return self.id_counter


broker = my_broker()

# The assertions below would continually fail (segfault) if it wasn't
# for the garbage collector fix in SQLite v3.8.6 and
# https://www.sqlite.org/c3ref/create_function_v2.html .
#
# Note that the code below would also segfault if the SQLite database
# is not closed (using "a.close()") in the callback function "my_cb".
#
