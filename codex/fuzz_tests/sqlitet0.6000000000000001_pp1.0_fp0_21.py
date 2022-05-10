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

cb = sqlite3.sqlite_int64_t(my_cb)

# find the sqlite3 shared library
sqlite3_lib = ctypes.util.find_library("sqlite3")
if not sqlite3_lib:
    raise Exception("Couldn't find sqlite3 library")

# load it
lib = ctypes.CDLL(sqlite3_lib)
if not lib:
    raise Exception("Couldn't load sqlite3 library")

# register the callback
lib.sqlite3_initialize()
lib.sqlite3_config(lib.SQLITE_CONFIG_SINGLETHREAD, ctypes.c_void_p(-1))
lib.sqlite3_config(lib.SQLITE_CONFIG_LOG, cb, ctypes.c_void_p(-1))

# create a database connection
conn = sqlite3.connect(DB_URI, uri=True)

# create a table
conn.execute("create table test(a, b)")

# insert a row
conn.execute("insert into test(
