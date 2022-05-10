import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, name VARCHAR(10))')
cursor.execute('INSERT INTO test VALUES (1, "foo")')
cursor.execute('INSERT INTO test VALUES (2, "bar")')
cursor.execute('SELECT * FROM test')
