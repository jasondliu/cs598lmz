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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, True)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD, True)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MEMSTATUS, False)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOOKASIDE, 0, 0)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb)

# Load the sqlite3.dll library
lib = ctypes.util.find_library('sqlite3')
lib = ctypes.CDLL(lib)

# Set the busy timeout
lib.sqlite3_busy_timeout(ctypes.c_void_p(0), 1000)

# Create a new database connection
conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

# Create a table
conn.execute("CRE
