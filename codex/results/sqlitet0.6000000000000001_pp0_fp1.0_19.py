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

def main():
    sqlite3.set_authorizer(my_cb)

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.execute("CREATE TABLE test(f1)")
    conn.execute("INSERT INTO test (f1) VALUES (test(1, 2))")
    conn.execute("SELECT * FROM test")

    ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(threading.current_thread().ident), ctypes.py_object(SystemExit))

    threading.Thread(target=conn.execute, args=("SELECT * FROM test",)).start().join()

    del conn

main()
