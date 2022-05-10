import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:') and
# sqlite3.connect('{}?mode=memory&cache=shared'.format(':memory:'))
# on OS X, the difference is that the former is
# thread-safe but not process-safe while the latter is
# both thread-safe and process-safe.

def thread_test(id):
    conn = sqlite3.connect(':memory:')
    conn.execute("""CREATE TABLE IF NOT EXISTS counter (id integer NOT NULL
        PRIMARY KEY, val integer NOT NULL);""")

    for i in range(1, 10001):
        conn.execute("INSERT INTO counter VALUES (?, ?);", (id, i))
        res = conn.execute("SELECT val from counter where id=?;", (id,)).fetchone()
        # Assert only 1 row is fetched
        assert(res[0] == i)

    conn.close()

t1 = threading.Thread(target=thread_test, args=(1,))
t2 = threading.Thread(target=thread_test, args=(2,))
