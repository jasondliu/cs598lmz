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
    lib = ctypes.util.find_library('sqlite3')
    if lib is not None:
        sqlite3 = ctypes.CDLL(lib)
        if sqlite3.sqlite3_threadsafe() != 0:
            print("Running this test in multiple threads")
            import threading
            threads = [threading.Thread(target=my_cb, args=(i,)) for i in range(10)]
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            print("Done")
        else:
            print("sqlite3 is not thread safe")
    else:
        print("sqlite3 not found")
