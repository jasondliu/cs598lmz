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

def my_cb_x(p):
    my_threading_local.a.close()
    return 1


def check(ans):
    print ("Checking...")
    conn = sqlite3.connect(DB_URI, uri=True)
    print (ans)

    c = conn.cursor()
    v = c.execute("select test(6,7)").fetchone()[0]
    print (v)

if __name__ == '__main__':
    sqlite3.sqlite3_open_v2(DB_URI, ctypes.pointer(my_threading_local.db_ptr),
                            sqlite3.SQLITE_OPEN_CREATE | sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_NOMUTEX,
                            "")

