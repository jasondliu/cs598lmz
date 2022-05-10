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
</code>
I have included a couple of different ways of trying to close the connection, but neither of them seem to work. I cannot find any Python documentation on this matter and I find it a bit odd that I cannot find any examples of this. Does anybody know how to close the connection properly?
I am using Python 3.4.3, but I believe the problem has been around for a long time.

