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

# Initialize the delete callback. This is only required if you're
# using Python 3.
sqlite3.sqlite3_initialize()
sqlite3.sqlite3_enable_load_extension(1)
lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_enable_load_extension.argtypes = (ctypes.c_void_p, ctypes.c_int)
lib.sqlite3_enable_load_extension(my_cb)
#
# Create a dummy table to force the connection to be open.
a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
cursor = a.cursor()
cursor.execute("CREATE TABLE foo(bar integer)")
cursor.execute("INSERT INTO foo(bar) values (1)")
cursor.close()

# Then, delete the connection and make a new one.
del a

a = sqlite3.connect(DB_URI, uri=True, factory=de
