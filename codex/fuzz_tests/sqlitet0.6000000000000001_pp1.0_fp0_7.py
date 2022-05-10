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

def test_init(p):
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb, 0)

    sqlite3.threadsafety = 1
    sqlite3.sqlite_version_info = sqlite3.sqlite_version.split('.')

    sqlite3.sqlite_version_info = [int(x) for x in sqlite3.sqlite_version_info[:3]]

    sqlite3.sqlite_version_info += [0] * (3 - len(sqlite3.sqlite_version_info))

    sqlite3.threadsafety = 2
    sqlite3.paramstyle = 'qmark'

    sqlite3.threadsafety = 3
    sqlite3.paramstyle = 'numeric'

    sqlite3.threadsafety = 4
    sqlite3.paramstyle = 'named'

    sqlite3.threadsafety = 5
    sqlite3.paramstyle = 'format'

    sqlite3.threadsafety = 6
    sqlite3.paramstyle = '
