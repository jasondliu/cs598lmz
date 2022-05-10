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

    return 12


sqlite3.sqlite3_open(b":memory:", ctypes.byref(my_threading_local.a))
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_enable_load_extension(my_threading_local.a, 0)
sqlite3.sqlite3_enable_load_extension(my_threading_local.a, 1)
sqlite3.sqlite3_db_config(my_threading_local.a, sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION, 1, ctypes.c_char_p())
sqlite3.sqlite3_load_extension(my_threading_local.a, ctypes.util.find_library('sqlite3'), "sqlite3_python_init", ctypes.c_void_p())

sqlite3.sqlite3_interrupt(my_threading_local.a)
sqlite3.sqlite3_busy_handler(
