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

my_cb_c = sqlite3.SQLITE_DETERMINISTIC(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb))

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SINGLETHREAD)
sqlite3.sqlite3_enable_load_extension(1)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_initialize()

conn = sqlite3.connect(DB_URI, uri=True)
conn.create_function("my_cb", 1, my_cb_c)
conn.execute("select my_cb(1)")

lib.sqlite3_shutdown()

conn.close()

# The bug: the a connection object is leaked, because it is not closed.
# In a multi-threaded environment, this would be a problem.
# In a single-threaded environment, it is not a problem.
