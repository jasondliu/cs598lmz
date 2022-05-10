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

sqlite3.enable_shared_cache(True)
sqlite3.set_authorizer(my_cb)

if __name__ == "__main__":
    import sys
    import time
    import threading

    def t():
        while True:
            with my_threading_local.a as a:
                c = a.cursor()
                c.execute("select test(3, 4)")
                for i in c:
                    print(i)
            time.sleep(0.1)

    threading.Thread(target=t).start()

    with sqlite3.connect(DB_URI, uri=True, factory=deleting_conn) as a:
        c = a.cursor()
        c.execute("select test(3, 4)")
        for i in c:
            print(i)
        time.sleep(0.1)
