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

ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_temp_directory()
sqlite3.sqlite_version

sqlite3.register_adapter(dict, sqlite3.Binary)
sqlite3.register_converter("dict", sqlite3.Binary)


conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
conn.create_function("my_cb", 1, my_cb)

def test_fn(a, b):
    return a

conn.create_function("test", 2, test_fn)

conn.execute("CREATE TABLE tbl (id INTEGER PRIMARY KEY AUTOINCREMENT, key TEXT UNIQUE, value dict)")

conn.execute("INSERT INTO tbl (key, value) VALUES (?, ?)", (b"a", b"hello"))
conn.execute("INSERT INTO tbl (key, value) VALUES (?, ?)", (b"b", {"hello": b"world"}))
conn
