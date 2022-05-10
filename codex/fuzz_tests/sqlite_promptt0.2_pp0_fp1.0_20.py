import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE test(id INTEGER PRIMARY KEY, name TEXT)')
cursor.execute('INSERT INTO test(name) VALUES (?)', ('foo',))
cursor.execute('INSERT INTO test(name) VALUES (?)', ('bar',))
cursor.execute('SELECT * FROM test')
print(cursor.fetchall())

# Test sqlite3.connect() with timeout
conn = sqlite3.connect(':memory:', timeout=1)
cursor = conn.cursor()
cursor.execute('CREATE TABLE test(id INTEGER PRIMARY KEY, name TEXT)')
cursor.execute('INSERT INTO test(name) VALUES (?)', ('foo',))
cursor.execute('INSERT INTO test(name) VALUES (?)', ('bar',))
cursor.execute('SELECT * FROM test')
print(cursor.fetchall())

# Test sqlite3.connect() with isolation_level
conn
