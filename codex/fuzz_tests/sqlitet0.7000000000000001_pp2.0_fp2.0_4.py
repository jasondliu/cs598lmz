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

    return 10

def main():
    import sys

    if sys.argv[1:]:
        count = int(sys.argv[1])
    else:
        count = 10

    sqlite3.enable_shared_cache(True)
    sqlite3.threadsafety = 2

    print("SQLite v%s" % (sqlite3.sqlite_version,))

    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    libc.on_exit(my_cb, None)

    def run_test(i):
        a = my_threading_local.a
        a.execute("SELECT test(1, 2)")
        a.execute("SELECT test(3, 4)")

    threads = [threading.Thread(target=run_test, args=(i,)) for i in range(count)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("OK")

if __name__ == "__main__":
    main()
