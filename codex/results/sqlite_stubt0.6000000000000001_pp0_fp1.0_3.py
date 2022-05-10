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

def my_cb2(p):
    my_threading_local.a.execute("select test(1, 2)")

    return 1

def my_cb3(p):
    my_threading_local.a.execute("select test(1, 2)")

    return 1

def main():
    assert ctypes.util.find_library("sqlite3")
    sqlite3.enable_callback_tracebacks(True)
    d = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    sqlite3.register_adapter(bool, int)
    sqlite3.register_adapter(float, repr)
    sqlite3.register_converter("bool", lambda s: bool(int(s)))
    sqlite3.register_converter("float", float)
    sqlite3.threadsafety = 3
    d.sqlite3_enable_load_extension(1)
    sqlite3.connection.enable_load_extension(1)
    sqlite3.enable_load_extension(
