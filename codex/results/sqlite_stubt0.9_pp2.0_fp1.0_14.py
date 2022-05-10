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


def python_start():
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    libc.exit(0)

def main():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.set_progress_handler(my_cb, 1000)

    cur = conn.execute("select 1, 2")
    print(cur)
    print(my_threading_local.a)
    print("i h")
    time.sleep(30)
    print("i ho")
    threading.Thread(target=python_start).start()
    print("i hol")
    time.sleep(30)
    print("i hold")
    time.sleep(30)
    print("i hol")
    time.sleep(30)
    print("i ho")
    time.sleep(30)
    print("i h")
    time.sleep(30)
    print("i ")
    time.sleep(30)

main()
</code>
When
