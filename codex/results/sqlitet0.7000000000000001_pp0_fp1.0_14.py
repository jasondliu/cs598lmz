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
    sqlite3.API_VERSION = (3, 8, 2)
    sqlite3.OPEN_READWRITE = 1
    sqlite3.OPEN_CREATE = 4
    sqlite3.OPEN_URI = 64
    sqlite3.SQLITE_OK = 0
    sqlite3.SQLITE_DONE = 101
    sqlite3.SQLITE_ROW = 100
    sqlite3.SQLITE_INTEGER = 1
    sqlite3.SQLITE_FLOAT = 2
    sqlite3.SQLITE_BLOB = 4
    sqlite3.SQLITE_NULL = 5
    sqlite3.SQLITE_DONE = 101
    sqlite3.SQLITE_ROW = 100
    sqlite3.SQLITE_ERROR = 1
    sqlite3.SQLITE_MISUSE = 21
    sqlite3.SQLITE_BUSY = 5
    sqlite3.SQLITE_READONLY = 8
    sqlite3.SQLITE_INTERRUPT = 9
   
