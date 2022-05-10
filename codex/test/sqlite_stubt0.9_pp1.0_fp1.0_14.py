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

# On OSX, this *must* be 'libsqlite3'
sqlite3.sqlite3_open(ctypes.util.find_library('sqlite3'), ctypes.byref(my_threading_local.handle));
sqlite3.sqlite3_create_function(my_threading_local.handle, b'test', 2, 1, None, my_cb, None, None)
sqlite3.sqlite3_open_v2(DB_URI.encode(), ctypes.byref(my_threading_local.handle), sqlite3.SQLITE_OPEN_URI, None)
sqlite3.sqlite3_close_v2(my_threading_local.handle)

print('done close')

del my_threading_local
