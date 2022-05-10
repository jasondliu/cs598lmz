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

sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_initialize()
libsqlite_filename = ctypes.util.find_library('sqlite3')
if not libsqlite_filename:
    raise Exception("Can't find sqlite3 library")
sqlite3.sqlite3_enable_shared_cache(1)

dns = sqlite3.sqlite3_enable_load_extension(1)

sqlite3.sqlite3_open(":memory:", ctypes.byref(my_threading_local.db))
sqlite3.sqlite3_close(my_threading_local.db)
sqlite3.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.db))

sqlite3.sqlite3_set_authorizer(my_threading_local.db, my_cb, 0)

conn = sqlite3.connect(DB_URI, uri=True)
conn.close()

if my_threading_local.a is not None
