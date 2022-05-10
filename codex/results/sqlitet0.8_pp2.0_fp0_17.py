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

sqlite3.sqlite_open_v2 = sqlite3.sqlite_open
sqlite3.sqlite_open = my_cb

conn = sqlite3.connect(DB_URI, uri=True)

def my_1():
    while True:
        try:
            conn.execute("select test(1, 2);")
        except Exception:
            pass

def my_2():
    while True:
        a = my_threading_local.a
        try:
            a.close()
        except Exception:
            pass

print("starting")

t = []

for _ in range(3):
    t.append(threading.Thread(target=my_1))

t.append(threading.Thread(target=my_2))

for th in t:
    th.start()

for th in t:
    th.join()

print("done")
