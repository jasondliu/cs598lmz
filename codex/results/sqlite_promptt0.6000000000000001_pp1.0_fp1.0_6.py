import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class Test(threading.Thread):
    def run(self):
        self.doit()

    def doit(self):
        while True:
            try:
                conn = sqlite3.connect(':memory:')
                cur = conn.cursor()
                cur.execute('CREATE TABLE t1 (a, b);')
                cur.execute('INSERT INTO t1 VALUES (?, ?);', (1, 2))
                cur.execute('INSERT INTO t1 VALUES (?, ?);', (2, 3))
                cur.execute('INSERT INTO t1 VALUES (?, ?);', (3, 4))
                cur.execute('SELECT * FROM t1;')
                print(cur.fetchall())
                conn.close()
            except:
                pass

for i in range(10):
    Test().start()
</code>


A:

The result of <code>ctypes.util.find_library('sqlite3')</code> must be <code>None</code>.
In this case, Python tries to find the library
