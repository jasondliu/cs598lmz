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
    sqlite3.sqlite3_thread_cleanup()
    p = ctypes.c_void_p()
    sqlite3.sqlite3_open(DB_URI, ctypes.byref(p))
    sqlite3.sqlite3_thread_cleanup()
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
    sqlite3.sqlite3_thread_cleanup()
    sqlite3.sqlite3_db_config(p, sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION, 1)
    sqlite3.sqlite3_thread_cleanup()
    sqlite3.sqlite3_create_function(p, "test_cb", 0, 1, None, my_cb, None, None)
    sqlite3.sqlite3_thread_cleanup()
    sqlite3.sqlite3_close(p)
    sqlite3.sqlite3_thread_cleanup()


