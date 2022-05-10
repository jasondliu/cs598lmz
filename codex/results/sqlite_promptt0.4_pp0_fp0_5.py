import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(':memory:')

# Test sqlite3.Cursor
cursor = conn.cursor()

# Test sqlite3.Connection.commit
conn.commit()

# Test sqlite3.Connection.close
conn.close()

# Test sqlite3.Connection.execute
cursor.execute('CREATE TABLE example(id INTEGER PRIMARY KEY, data TEXT)')

# Test sqlite3.Connection.executemany
cursor.executemany('INSERT INTO example(data) VALUES (?)',
                   [('Hello',), ('World',)])

# Test sqlite3.Connection.execute
cursor.execute('SELECT id, data FROM example')

# Test sqlite3.Cursor.fetchall
cursor.fetchall()

# Test sqlite3.Cursor.fetchone
cursor.fetchone()

# Test sqlite3.Cursor.fetchmany
cursor.fetchmany()

# Test sqlite3.Cursor.fetchmany
cursor.f
