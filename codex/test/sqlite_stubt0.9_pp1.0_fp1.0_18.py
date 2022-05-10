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

def test_concurrent_access_redesigned():
    result = True

    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    my_cb_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

    t1 = threading.Thread(target=libc.printf,
                          args=(b"thread1\n",),
                          kwargs={"callback": my_cb_c})
    t2 = threading.Thread(target=libc.printf,
                          args=(b"thread2\n",),
                          kwargs={"callback": my_cb_c})

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return result

def main():
    res = test_concurrent_access_redesigned()
    print("Result:", res)

if __name__ == "__main__":
    main()
