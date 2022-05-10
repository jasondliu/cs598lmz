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

def main(argc, argv):
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.load_extension(
        ctypes.util.find_library("mod_sqlite3"),
        "mod_sqlite3_init")

    p = sqlite3.prepare("select sqlite3_db_config(?, ?)")
    p.set("threading_local", 1)
    sqlite3.executescript("attach '%s' as db create temp table t1(n);" % argv[1])

    sqlite3.executescript("insert into t1 values (10);")
    sqlite3.execute("db", "insert into t1 values (20);")

    cur = sqlite3.execute("select * from t1;")
    assert cur.fetch() == (10,)
    assert cur.fetch() == (20,)

    p = sqlite3.prepare("db", "select * from t1;")

