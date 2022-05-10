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

if __name__ == '__main__':
    lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_shutdown()
    lib.sqlite3_config(lib.SQLITE_CONFIG_URI, 1)

    my_cb_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(my_cb)

    lib.sqlite3_initialize()
    print(lib.sqlite3_open_v2(DB_URI.encode(), ctypes.byref(my_threading_local.db), lib.SQLITE_OPEN_READWRITE | lib.SQLITE_OPEN_CREATE | lib.SQLITE_OPEN_MEMORY | lib.SQLITE_OPEN_URI | lib.SQLITE_OPEN_SHAREDCACHE | lib.SQLITE_OPEN_NOMUTEX, None))

    my_threading_local.db.contents = lib.sqlite3_db_handle(my_threading
