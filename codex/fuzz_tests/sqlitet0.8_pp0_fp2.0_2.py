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

    return 100

def main():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.set_step_callback(my_cb)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE tests(aa INTEGER, bb INTEGER)")
    cursor.execute("INSERT INTO TESTS(aa, bb) VALUES(1, 1), (2, 2), (3, 3), (4, 4)")
    cursor.execute("SELECT * FROM TESTS")
    conn.close()

if __name__ == "__main__":
    try:
        main()
    except:
        import sys
        print sys.exc_info()
        import pdb
        pdb.post_mortem()
