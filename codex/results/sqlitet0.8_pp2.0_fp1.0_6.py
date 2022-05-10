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
    SQLITE_CONFIG_SINGLETHREAD = 1

    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_config(SQLITE_CONFIG_SINGLETHREAD)

    sqlite3.sqlite3_commit_hook(my_cb, None)
    sqlite3.sqlite3_rollback_hook(my_cb, None)

    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    b.execute("CREATE TABLE foo (bar INTEGER)")
    b.execute("INSERT INTO foo VALUES (1), (2)")
    b.commit()

    b.execute("insert into foo select test(bar, ?) from foo", (1,))

    print(my_threading_local.a.execute("select * from foo").fetchall())

main()
