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
    my_cb_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    my_cb_p = ctypes.c_void_p(my_cb_c)

    libc = ctypes.CDLL(ctypes.util.find_library("c"))

    libc.on_new_thread(my_cb_p)

    t1 = threading.Thread(target=libc.start_new_thread)
    t1.start()

    t1.join()

    a = my_threading_local.a

    print(a)

    a.execute("SELECT test(1, 2)").fetchall()

    print(a)

if __name__ == "__main__":
    main()
</code>

