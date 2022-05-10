import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#conn = sqlite3.connect(':memory:')
#cursor = conn.cursor()
#cursor.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)')
#cursor.execute('INSERT INTO users(name) VALUES("Tom")')
#cursor.execute('INSERT INTO users(name) VALUES("Bob")')
#cursor.execute('INSERT INTO users(name) VALUES("Alice")')
#cursor.execute('SELECT * FROM users')
#for row in cursor:
#    print(row)
#conn.commit()
#conn.close()

# Test sqlite3.connect()
#conn = sqlite3.connect(':memory:')
#cursor = conn.cursor()
#cursor.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)')
#id_list = [(1, 'Tom'), (2, 'Bob'), (3, 'Alice')]
#cursor.executemany('INSERT INTO users(id, name) VALUES (?, ?)
