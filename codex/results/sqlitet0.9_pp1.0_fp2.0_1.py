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
    lib = ctypes.pythonapi.PyCObject_Import("lib", "lib")
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    res = libc.malloc(3)
    libc.free(res)
    lib.test_fn()
    print("test")

if __name__ == '__main__':
    main()
    threading.Thread(target=main).start()
</code>
The idea is to force the garbage collector to run in the <code>main</code> method, after which the <code>deleting_conn</code> instances will be deleted in the created thread. This causes a segfault. The same code without the <code>lib.dll</code> works correctly. 
The segfault I'm getting is at the <code>self.close()</code> line in the <code>deleting_conn.__del__</code> method. It looks like the GC is deleting the <code>sqlite3.Connection</code> instance before the <code>_
