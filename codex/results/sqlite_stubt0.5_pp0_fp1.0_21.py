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
    print(ctypes.util.find_library("sqlite3"))
    print(ctypes.util.find_library("sqlite"))
    print(ctypes.util.find_library("sqlite3.dll"))
    print(ctypes.util.find_library("sqlite.dll"))
    print(ctypes.util.find_library("libsqlite3"))
    print(ctypes.util.find_library("libsqlite"))
    print(ctypes.util.find_library("libsqlite3.so"))
    print(ctypes.util.find_library("libsqlite.so"))

    sqlite3.sqlite_version_info
    sqlite3.sqlite_version
    sqlite3.threadsafety
    sqlite3.paramstyle

    sqlite3.connect(DB_URI, uri=True)

    sqlite3.register_adapter(int, lambda a: str(a))
    sqlite3.register_adapter(str, lambda a: a.encode("utf-8
