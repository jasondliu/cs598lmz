import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() and sqlite3.Cursor()
connection = sqlite3.connect('/tmp/test.db', check_same_thread = False)
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Foo (x int)')
cursor.execute('INSERT INTO Foo VALUES (?)', (1234,))
cursor.execute('SELECT * from Foo')
print(cursor.fetchone())
cursor.close()
connection.close()

# Test sqlite3.Row
connection = sqlite3.connect('/tmp/test.db', check_same_thread = False)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()
cursor.execute('SELECT * from Foo')
r = cursor.fetchone()
print(r)
print(r['x'])
print(r[0])
cursor.close()
connection.close()

# Test custom type (str)
connection = sqlite3.connect('/tmp/test.db', check_same_thread = False)
c
