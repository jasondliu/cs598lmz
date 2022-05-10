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

def main():
    p = ctypes.util.find_library("sqlite3")
    sqlite3.sqlite3_open_v2(p, DB_URI, 1, None)
    sqlite3.sqlite3_enable_load_extension(sqlite3.sqlite3_db_handle(my_threading_local.a), 1)
    sqlite3.sqlite3_load_extension(my_threading_local.a, "./test.so", "sqlite3_extension_init", None)
    sqlite3.sqlite3_enable_load_extension(sqlite3.sqlite3_db_handle(my_threading_local.a), 0)
    my_threading_local.a.execute("select test(1, 2)")
    my_threading_local.a.commit()
    my_threading_local.a.close()

main()
