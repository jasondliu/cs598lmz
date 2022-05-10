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

def my_thread():
    z = my_threading_local.a.execute("SELECT test(10, 15)")
    my_threading_local.a.commit()
    assert z.fetchone()[0] == 10

def test_simple():
    driver = sqlite3.get_throttle_driver()
    old_sqlite_progress_handler = driver.sqlite_progress_handler

    driver.sqlite_progress_handler = my_cb

    t = threading.Thread(target=my_thread)
    t.start()
    t.join()

    driver.sqlite_progress_handler = old_sqlite_progress_handler
</code>


A:

Avoid creating threading-local connections
You shouldn't make new connections in the <code>sqlite_progress_handler</code> handler. From the documentation:
<blockquote>
<p>A critical error occurs if the sqlite_progress_handler() callback of a prepared statement attempts to re-enter the same prepared statement.</p>
</blockquote>
What's happening is that your <code
