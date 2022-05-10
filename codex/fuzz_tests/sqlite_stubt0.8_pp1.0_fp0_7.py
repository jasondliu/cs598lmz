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

if __name__ == "__main__":
    path = ctypes.util.find_library("sqlite3")
    label = ctypes.c_char_p(b"mylib")
    clib = ctypes.CDLL(path, use_errno=True, use_last_error=True)

    # Register an error logger routine
    clib.sqlite3_config(ctypes.c_uint(3), my_cb, label)

    try:
        a = sqlite3.connect(DB_URI, uri=True)
        a.execute("select test(?, ?)", (1, 2))
    except:
        pass

    a = my_threading_local.a

    cur = a.execute("select * from sqlite_master;")
    data = cur.fetchall()
    print('main:', data)

    try:
        a.execute("select test(?, ?)", (1, 2))
    except:
        pass
