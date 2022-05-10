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

def my_err_cb(p):
    raise sqlite3.OperationalError("")

sqlite3.sqlite3_sqlite3_config(
    sqlite3.SQLITE_CONFIG_RESTRICTED_VFS, 1,
    ctypes.c_char_p(b"test"))

sqlite3.sqlite3_sqlite3_config(
    sqlite3.SQLITE_CONFIG_VFS,
    ctypes.c_char_p(b"test"),
    ctypes.c_char_p(ctypes.util.find_library("sqlite3")),
    ctypes.c_char_p(b":testvfs"))

sqlite3.sqlite3_sqlite3_vfs_register(
    my_cb, my_err_cb, None, None, None, None, None, None)

with sqlite3.connect(DB_URI, uri=True) as c:
    c.execute("CREATE TABLE test(id integer primary key)")
    c.execute("SELECT test(?,
