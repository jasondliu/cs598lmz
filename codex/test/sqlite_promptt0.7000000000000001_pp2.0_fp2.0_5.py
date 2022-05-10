import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE person (id INTEGER, name STRING)')
cursor.execute('INSERT INTO person (id, name) VALUES (?, ?)', (1, 'Joe'))
cursor.execute('INSERT INTO person (id, name) VALUES (?, ?)', (2, 'Jane'))
cursor.execute('SELECT * FROM person')
