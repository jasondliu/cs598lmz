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

my_cb(None)

# A second thread
t = threading.Thread(target=my_cb, args=(None,))
t.start()
t.join()

# MUST have a way  to reinitialize a new thread in pysqlite which has
# its very own copy of the Python objects created in my_cb.  This is
# because pysqlite uses Python's "threading_local" concept, which means
# that each thread has its own copy of the Python objects.

# In this particular case, a function object bound to a connection
# object was created by my_cb, and stored into a threading local.

# A segfault happens when this cache of the function object is shared
# amongst the other threads.

# This testcase is just one possible way to segfault.  The segfault can
# also happen when a thread has a function object bound to a connection,
# and then a seperate thread later takes over that thread, and uses the
# connection object.

# The segfault is caused by the detach()/attach()
