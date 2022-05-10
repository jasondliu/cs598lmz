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

# We start the sqlite3 runtime.
sqlite3.threadsafety = 0
sqlite3.enable_load_extension(True)

# Try to load the extension.
lib = ctypes.CDLL("libtest")
lib.do_something(my_cb)

# Check the extension.
a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.create_aggregate("test", 2, lambda: ())

# Now, we tear down the extension.
lib.tear_down()

# And check it was torn down correctly.
a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
with pytest.raises(sqlite3.OperationalError):
    a.create_aggregate("test", 2, lambda: ())

a.close()
