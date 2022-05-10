import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)')
c.execute('INSERT INTO test VALUES (1, "test")')
conn.commit()
c.execute('SELECT * FROM test')
print(c.fetchone())
conn.close()

# Test sqlite3.connect(..., detect_types=sqlite3.PARSE_DECLTYPES)
conn = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
c = conn.cursor()
c.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT, dt TIMESTAMP)')
c.execute('INSERT INTO test VALUES (1, "test", CURRENT_TIMESTAMP)')
conn.commit()
c.execute('SELECT * FROM test')
print(c.fetchone())
conn.close()

# Test sqlite3.connect(...,
