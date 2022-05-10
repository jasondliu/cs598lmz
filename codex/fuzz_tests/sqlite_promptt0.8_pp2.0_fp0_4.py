import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:?cache=shared").
import multiprocessing

def f():
    conn = sqlite3.connect("file::memory:?cache=shared")
    c = conn.cursor()
    c.execute("CREATE TABLE test (x)")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"), mode=ctypes.RTLD_GLOBAL)
    lib.sqlite3_enable_shared_cache(1)
    pool = multiprocessing.Pool(initializer=f, initargs=())
    pool.map(f, range(10))
