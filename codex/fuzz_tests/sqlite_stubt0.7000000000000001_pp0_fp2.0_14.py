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

p = lib.sqlite3_enable_shared_cache(1)
print "shared cache:", p
if p != 1:
    print "failed to enable shared cache"
    sys.exit(1)

lib.sqlite3_config(lib.SQLITE_CONFIG_URI, 1)

lib.sqlite3_config(lib.SQLITE_CONFIG_SINGLETHREAD)
p = lib.sqlite3_config(lib.SQLITE_CONFIG_GETMALLOC, ctypes.byref(sz))
print "sz:", sz.value

lib.sqlite3_config(lib.SQLITE_CONFIG_MALLOC, ctypes.byref(sz))

lib.sqlite3_initialize()

lib.sqlite3_config(lib.SQLITE_CONFIG_SQLLOG, my_cb)

p = lib.sqlite3_threadsafe()
print "threadsafe:", p

lib.sqlite3_config(lib.SQLITE_CONFIG_MULTITHREAD)
p
