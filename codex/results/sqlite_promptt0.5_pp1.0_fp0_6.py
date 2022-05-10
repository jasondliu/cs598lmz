import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
db = sqlite3.connect(':memory:')
cursor = db.cursor()
cursor.execute('CREATE TABLE names (id INTEGER PRIMARY KEY, name TEXT)')
cursor.execute('INSERT INTO names (name) VALUES (?)', ('John',))
cursor.execute('INSERT INTO names (name) VALUES (?)', ('George',))
cursor.execute('INSERT INTO names (name) VALUES (?)', ('Paul',))
cursor.execute('INSERT INTO names (name) VALUES (?)', ('Ringo',))
cursor.execute('SELECT * FROM names')
for row in cursor:
    print(row)

cursor.execute('SELECT * FROM names')
rows = cursor.fetchall()
print(rows)

cursor.execute('SELECT * FROM names')
for row in cursor.fetchall():
    print(row)

cursor.execute('SELECT * FROM names')
rows = cursor.fetchmany(2)
print(rows)

cursor.execute('SELECT * FROM names')
rows
