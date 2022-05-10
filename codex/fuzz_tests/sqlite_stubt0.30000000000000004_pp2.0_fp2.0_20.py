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

def my_thread_fn():
    my_threading_local.a.execute("SELECT test(1, 2)")

def main():
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))
    lib.sqlite3_enable_shared_cache(ctypes.c_int(1))
    lib.sqlite3_initialize()

    lib.sqlite3_enable_load_extension(ctypes.c_int(1))

    lib.sqlite3_auto_extension(ctypes.c_void_p(my_cb))

    threads = []

    for i in range(10):
        t = threading.Thread(target=my_thread_fn)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
