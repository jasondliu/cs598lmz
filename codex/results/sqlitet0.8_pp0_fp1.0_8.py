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

def my_init(_):
    ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_db_config(my_threading_local.a.db, 3, 1, 1)

sqlite3.register_adapter(float, lambda x: str(x))
sqlite3.register_adapter(int, lambda x: str(x))
sqlite3.register_adapter(str, lambda x: x)
sqlite3.register_converter("float", float)
sqlite3.register_converter("int", int)
sqlite3.register_converter("str", str)

sqlite3.sqlite_version_info
sqlite3.threadsafety
sqlite3.PARSE_DECLTYPES
sqlite3.PARSE_COLNAMES

sqlite3.sqlite_version

conn = sqlite3.connect(":memory:", factory=deleting_conn, detect_types=sqlite3.PARSE_DECLTYPES)

cur = conn.c
