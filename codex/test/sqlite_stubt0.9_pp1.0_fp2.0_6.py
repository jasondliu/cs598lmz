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

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
libsqlite3.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p),
                                      ctypes.c_int, ctypes.c_char_p]

with sqlite3.connect(DB_URI, uri=True) as conn1:
    conn1.set_progress_handler(my_cb, 111)
    cursor = conn1.execute("select 123")
    value = cursor.fetchone()
    print("value:",value)
    del cursor

    for i in range(1,10):
        print("attempt:",i)
        with sqlite3.connect(DB_URI, uri=True) as conn2:
            cursor2 = conn2.execute("select * from sqlite_master")
            value2 = cursor2.fetchone()
            print("value2:",value2)
            del cursor2

db_
