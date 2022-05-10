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

if __name__ == "__main__":
    print(ctypes.util.find_library("sqlite3"))
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb)
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.close()

    my_conn = my_threading_local.a

    # create some more threads and verify that we don't get any segfaults
    def thread_fn():
        c = my_conn.cursor()
        c.execute("SELECT test(?,?)", (1, 2))
        c.close()

    threads = []
    for i in range(10):
        t = threading.Thread(target=thread_fn)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
