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
    print(my_threading_local.a)

def my_cb3(p):
    print(my_threading_local.a)

def helper():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_shared_cache(1)

    th1 = threading.Thread(target=my_cb)
    th2 = threading.Thread(target=my_cb2)
    th3 = threading.Thread(target=my_cb3)

    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()


if __name__ == "__main__":
    helper()
</code>
I've tried using <code>create_aggregate</code> to circumvent the problem, but the aggregate function would only get called on one thread, the others throw <code>OperationalError: no such function: test</code>.

