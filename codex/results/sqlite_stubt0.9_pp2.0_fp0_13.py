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

print "Loading SQLite library..."
sqlite3.sqlite_api._sqlite_init(ctypes.create_string_buffer(10), ctypes.pointer(ctypes.c_int(0)), my_cb, None)
print "Sleeping for 2 seconds..."
time.sleep(2)
print "Killing SQLite library..."
sqlite3.sqlite_api._sqlite_fini()
