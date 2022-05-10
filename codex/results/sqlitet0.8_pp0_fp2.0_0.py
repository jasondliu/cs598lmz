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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(4))
lib.sqlite3_enable_shared_cache(ctypes.c_int(1))

db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
db.executescript(
    """
    CREATE TABLE test (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        a INTEGER,
        b INTEGER,
        c INTEGER,
        d INTEGER,
        e INTEGER,
        f INTEGER
    );

    CREATE TRIGGER test_i AFTER INSERT ON test
    BEGIN
        SELECT test(NEW.a, NEW.b);
    END;
    """
)

db.create_function("test", 2, test_fn)

my_threading_local.a = db

my_cb(ctypes.c
