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

sqlite3.sqlite3_open(DB_URI, ctypes.pointer(my_threading_local.a))
sqlite3.sqlite3_open_v2(DB_URI, ctypes.pointer(my_threading_local.a),
                        sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE, None)
sqlite3.sqlite3_busy_handler(my_threading_local.a, my_cb, None)

sqlite3.sqlite3_close(my_threading_local.a)

sqlite3.sqlite3_threadsafe()

sqlite3.sqlite3_enable_shared_cache(1)

sqlite3.sqlite3_initialize()
sqlite3.sqlite3_shutdown()

sqlite3.sqlite3_sleep(1)

sqlite3.sqlite3_get_autocommit(my_threading_local.a)

sqlite3.sqlite3_db_handle(my_
