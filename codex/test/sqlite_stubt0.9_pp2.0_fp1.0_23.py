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

def main(argc, argv):
    cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)(my_cb)

    odb = ctypes.c_void_p()

    testlib = ctypes.CDLL(ctypes.util.find_library("testlib"))
    testlib.sqlite3_open(ctypes.c_char_p(DB_URI), ctypes.pointer(odb))

    with sqlite3.connect(DB_URI, uri=True) as conn:
        with conn.execute("""
            create table test(a int primary key, b text);
            begin;
            insert into test values (1, "a");
            """) as cur:
            cur.testcb = cb

            for _ in cur.execute("select test(a, b) from test"):
                pass

        with conn.execute("""
            insert into test values (2, "b");
            """) as cur:
            my_threading_local.a.rollback()

