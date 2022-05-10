import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)''')
c.execute('''INSERT INTO test VALUES (1, 'foo')''')
c.execute('''INSERT INTO test VALUES (2, 'bar')''')
c.execute('''INSERT INTO test VALUES (3, 'baz')''')
c.execute('''INSERT INTO test VALUES (4, 'qux')''')
c.execute('''INSERT INTO test VALUES (5, 'quux')''')
c.execute('''INSERT INTO test VALUES (6, 'corge')''')
c.execute('''INSERT INTO test VALUES (7, 'grault')''')
c.execute('''INSERT INTO test VALUES (8, 'garply')''')
c.execute('''INSERT INTO test VALUES (9, 'waldo')''')
c.execute('''INSERT INTO test
