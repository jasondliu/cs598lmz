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

def my_close_cb(ud):
    try:
        my_threading_local.a.close()
    except AttributeError:
        pass
    finally:
        del my_threading_local.a
    return 1

sqlite3._sqlite.sqlite3_open_v2(bytes(DB_URI, 'UTF-8'), ctypes.byref(my_threading_local.a),
                                sqlite3._sqlite.SQLITE_OPEN_URI | sqlite3._sqlite.SQLITE_OPEN_MEMORY | sqlite3._sqlite.SQLITE_OPEN_CREATE,
                                None)
sqlite3._sqlite.sqlite3_enable_shared_cache(True)
sqlite3._sqlite.sqlite3_open_callback(my_cb, None, None)
sqlite3._sqlite.sqlite3_close_callback(my_close_cb, None)

sqlite3._sqlite.sqlite3_config(sqlite3._sqlite.SQLITE_CONFIG_MULT
