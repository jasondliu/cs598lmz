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

if "my_cb" not in sqlite3.sqlite_api.__dict__:
    raise Exception("need sqlite3.register_adapter")

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(4, my_cb, 1)

def autocommit_cb(conn):
    conn.isolation_level = None

sqlite3.connect(DB_URI, uri=True, factory=deleting_conn, isolation_level=None, check_same_thread=False)
sqlite3.Connection.register_hook(autocommit_cb)

print("A")

def test1():
    b = my_threading_local.a.cursor()
    b.execute("select test_fn(?);", (1, ))
    row = b.fetchone()

    if row[0] != 1:
        raise Exception("%r != 1" % (row[0], ))

test1()

def test2():
    b =
