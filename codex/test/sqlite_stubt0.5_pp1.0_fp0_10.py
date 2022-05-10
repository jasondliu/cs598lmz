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
    ctypes.pythonapi.Py_Initialize()

    sqlite3.sqlite_version_info
    sqlite3.sqlite_version
    sqlite3.sqlite_source_id

    try:
        sqlite3.enable_callback_tracebacks(1)
    except AttributeError:
        pass

    sqlite3.threadsafety
    sqlite3.paramstyle

    sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    sqlite3.register_adapter(dict, lambda x: x)
    sqlite3.register_converter("dict", lambda x: x)

    sqlite3.complete_statement("select 1")

    sqlite3.connect(DB_URI, uri=True, factory=deleting_conn).interrupt()

    sqlite3.connect(DB_URI, uri=True, factory=deleting_conn).set_authorizer(lambda *args: 0)

