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

def my_cb_2(p):
    a = my_threading_local.a

    a.execute("CREATE TABLE test (a int, b int)")
    a.commit()

    a.execute("INSERT INTO test VALUES (?, ?)", (1, 2))
    a.commit()

    a.execute("SELECT * FROM test")
    assert a.fetchone() == (1, 2)

    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.optimize_tracebacks(True)

    path = ctypes.util.find_library('sqlite3')
    if path is None:
        raise RuntimeError("Can't find the sqlite3 library")
    sqlite3 = ctypes.CDLL(path)
    sqlite3.sqlite3_enable_shared_cache(0)

    sqlite3.sqlite3_config(3)

    cb = sqlite3.sqlite3_progress_handler(ctypes.c_int(1), ctypes.c_int(
