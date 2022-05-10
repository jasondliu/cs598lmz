import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:"), connection shared for all instances
# in the same thread
# From http://docs.python.org/2/library/sqlite3.html
# Test sqlite3.connect(None), see http://blog.mdda.net/rome/203

threads_done = 0
threads_error = 0

def test_n_threads(n):
    global threads_done
    global threads_error

    # sqlite3.connect(None) ==> memory database, connections
    # globally shared between threads of the same process
    tests = [sqlite3.connect(None) for i in range(n)]
    print "%d connections to sqlite3.connect(None)" % len(tests)

    def test_it(i):
        # This test executes n transactions that insert n rows
        # in n separate threads
        # sqlite3.connect(None) gives different connections
        # that share the same underlying database
        try:
            db = tests[i]
            for i in range(n):
                db.execute("insert into tbl%d values(?)
