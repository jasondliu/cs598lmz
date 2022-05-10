import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, value INTEGER)''')
c.execute('''INSERT INTO test (value) VALUES (1)''')
conn.commit()
c.execute('''SELECT * FROM test''')
print(c.fetchall())
conn.close()

# Test sqlite3.connect(':memory:')
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE test (id INTEGER PRIMARY KEY, value INTEGER)''')
c.execute('''INSERT INTO test (value) VALUES (1)''')
conn.commit()
c.execute('''SELECT * FROM test''')
print(c.fetchall())
conn.close()

# Test sqlite3.connect(':memory:', check_same_thread=False)
conn = sqlite3.connect(
