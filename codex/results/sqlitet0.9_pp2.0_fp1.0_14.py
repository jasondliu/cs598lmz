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

sqlite3.sqlite3_enable_shared_cache(0)
ctx = sqlite3.sqlite3_create_disposable_module(ctypes.CDLL(ctypes.util.find_library('sqlite3')), ctypes.c_char_p(DB_URI.encode()), "test", my_cb, ctypes.c_void_p(None))

my_threading_local.a.execute("select test(test(test(test(test(test(test(test(test('test')))))))))").fetchall()[0][0]

threads = []

while len(threads) < 256:
    t = threading.Thread(target=lambda: my_threading_local.a.execute("select test('test')").fetchall()[0][0])
    t.start()
    threads.append(t)

for i in threads:
    i.join()

threads = []

while len(threads) < 256:
    t = threading.Thread(target=lambda: my_thread
