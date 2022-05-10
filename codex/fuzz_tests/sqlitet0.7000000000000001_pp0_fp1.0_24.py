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

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

lib.sqlite3_shutdown()
lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))

lib.sqlite3_open_v2(ctypes.c_char_p(DB_URI.encode('utf-8')), ctypes.byref(my_threading_local.a), ctypes.c_int(0x1), ctypes.c_char_p(None))
lib.sqlite3_enable_load_extension(my_threading_local.a, 1)

lib.sqlite3_initialize()
lib.sqlite3_db_config(my_threading_local.a, ctypes.c_int(7), 1, 0)

lib.sqlite3_load_extension(my_threading_local.a, ctypes.c_char_p("./pysqlite_extension/build/lib.linux-x86_64-2
