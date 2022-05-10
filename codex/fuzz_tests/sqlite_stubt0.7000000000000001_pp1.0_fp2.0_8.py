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
    sqlite3.set_autocommit(False)
    sqlite3.enable_shared_cache(True)
    sqlite3.enable_load_extension(True)
    sqlite3.set_authorizer(None)
    sqlite3.set_progress_handler(my_cb, 100)

    sqlite3.threadsafety()
    sqlite3.sqlite_version_info
    sqlite3.sqlite_version
    sqlite3.PARSE_DECLTYPES
    sqlite3.PARSE_COLNAMES
    sqlite3.OPEN_READONLY
    sqlite3.OPEN_READWRITE
    sqlite3.OPEN_CREATE
    sqlite3.Connection()
    sqlite3.Row
    sqlite3.Cursor()
    sqlite3.Binary
    sqlite3.register_converter("t", lambda x: x)
    sqlite3.register_adapter(str, lambda x: x)
    sqlite3.adapt(str, "t")

