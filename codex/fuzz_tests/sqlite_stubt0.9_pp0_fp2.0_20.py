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

def my_enc_cb(p):
    if my_threading_local.a.execute("SELECT test('lala', 'lala')").fetchone()[0] != 'lala':
        raise Exception("Function failed to execute in correct context")

    my_threading_local.a = None

    return 1

def my_dec_cb(p):
    return 5

class EncThread(threading.Thread):
    def run(self):
        x = ctypes.cast(xtea, ctypes.cdll[ctypes.util.find_library("sqlite3")])
        x.sqlite3_key_v2(":memory:", ctypes.create_string_buffer(b"foobar"), 6, 0)
        my_threading_local.a.cursor().execute("CREATE TABLE test (id INTEGER PRIMARY KEY);")
        my_threading_local.a.cursor().execute("INSERT INTO test VALUES (?)", (5,))
        for row in my_threading_local.a.cursor().
