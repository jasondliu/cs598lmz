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

def key_cb(p, file_name):
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    b.create_function("test", 2, test_fn)

    return threading.current_thread().ident

# Set up the sqlite3 extension loading threading
sqlite3.enable_callback_tracebacks(True)
handles = sqlite3._sqlite.set_authorizer(my_cb)
handles = sqlite3._sqlite.set_sqlite3_key(key_cb)

try:
    sqlite3.load_extension(ctypes.util.find_library("example"), "sqlite3_helloworld_init")
except sqlite3.DatabaseError as e:
    print(str(e))
