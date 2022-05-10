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

ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_progress_handler(
    my_threading_local.a.connection, 20, my_cb, 1)

# When this is valid, it prevents the race
#print my_threading_local.a.total_changes
</code>
I guess I could get around the threading problem a different way... But I'd kinda like to know how to handle the problem I was originally trying to solve.


A:

I just had to stop subclassing the Connection object. I'm not sure why subclassing causes problems. Maybe because the connection object can't be casted to a <code>sqlite3_conn</code>.
<code>import ctypes
import ctypes.util
import threading
import sqlite3


my_threading_local = threading.local()

# This is a way to be able to create temporary files using sqlite
DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI
