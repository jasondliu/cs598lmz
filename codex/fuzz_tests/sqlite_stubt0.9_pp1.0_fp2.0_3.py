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

def my_init(dbapi_con, con_record):
    my_cb("Hello, world")

try:
    # make sure the backport is in use, not the C-extension
    import sqlalchemy.sqlite.dbapi2 as dbapi2
    assert dbapi2.__name__ != 'sqlite3'
except ImportError:
    pass

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(ctypes.c_int(2), ctypes.c_int(2))
sqlite3.sqlite_version = "3.7.0"
sqlite3.sqlite_version_info = (3, 7, 0)

dbapi2.register_adapter(sqlite3.Row, lambda row: tuple(row))
dbapi2.register_converter("BINARY", lambda data: buffer(data))

sqlite3.connect = lambda *a, **k: dbapi2._sqlite_connect(
    dbapi2.SQLiteConnection,
