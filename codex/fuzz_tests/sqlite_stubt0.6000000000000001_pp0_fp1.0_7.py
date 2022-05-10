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
    sqlite3.sqlite3_open("test.db", ctypes.byref(my_threading_local.db_ptr))
    sqlite3.sqlite3_create_function(my_threading_local.db_ptr, "my_cb", 1,
                                    0, None, my_cb)
    sqlite3.sqlite3_exec(my_threading_local.db_ptr, "select my_cb(1)",
                         None, None, None)
    sqlite3.sqlite3_close(my_threading_local.db_ptr)

main()
