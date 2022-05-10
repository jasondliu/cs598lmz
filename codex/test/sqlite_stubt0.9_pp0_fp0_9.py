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

def my_cb_close(p):
    a = my_threading_local.a
    my_threading_local.a = None
    return 1

# load sqlite dynamically
libfile = ctypes.util.find_library('sqlite3')
if libfile:
    sqlite3.sqlite_version_info = tuple(map(int, ctypes.CDLL(libfile).sqlite3_version.decode().split('.')))
    sqlite3.sqlite_version = ".".join(map(str, sqlite3.sqlite_version_info))

DB_URI = "file:test?mode=memory"

# connect
a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.executescript("""
    create table abc (a text);
insert into abc (a) values (1);
""")

a.create_function("test_cb_delete", 0, my_cb, my_cb_close)

