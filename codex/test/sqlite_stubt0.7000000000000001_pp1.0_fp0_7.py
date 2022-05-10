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

def my_cb2(p):
    #my_threading_local.a.close()
    del my_threading_local.a

# Create the database.
c = sqlite3.connect(DB_URI, uri=True)

# Create a couple of functions.
c.create_function("my_cb", 0, my_cb)
c.create_function("my_cb2", 0, my_cb2)

# Call the functions.
c.execute("select my_cb()")
c.execute("select my_cb2()")

# Attempt to close the database.
c.close()
