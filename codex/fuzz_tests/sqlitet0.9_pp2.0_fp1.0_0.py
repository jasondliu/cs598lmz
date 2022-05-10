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

def test_t():
    global my_threading_local
    while True:
        my_threading_local.a.execute("SELECT test(1, 2)")

CREATE_SQL = """CREATE TABLE foo (
  value INTEGER
);"""

INSERT_SQL = "INSERT INTO foo VALUES (?)"

def main(n, name):
    print(name)

    sqlite3.enable_callback_tracebacks(True)

    cb = sqlite3.SQLITE_DBCONFIG_TRACE
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.dbconfig_enable("tsi1", True)
    conn.dbconfig_enable_fkey(True)

    conn.execute(CREATE_SQL)

    t = threading.Thread(target=test_t, daemon=True)
    t.start()

    for _ in range(n):
        conn.execute(INSERT_SQL, (random.randrange(1, 1000000),))


