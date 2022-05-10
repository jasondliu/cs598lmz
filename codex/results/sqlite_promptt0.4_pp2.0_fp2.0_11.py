import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(':memory:')

# Test sqlite3.Row
cursor = conn.cursor()
cursor.execute('CREATE TABLE test(id INTEGER PRIMARY KEY, value TEXT)')
cursor.execute('INSERT INTO test (value) VALUES (?)', ('test',))
cursor.execute('SELECT * FROM test')
row = cursor.fetchone()
print(row.keys())
print(row['id'], row['value'])

# Test sqlite3.Connection.create_function
conn.create_function('double', 1, lambda x: x*2)
cursor.execute('SELECT double(?)', (21,))
print(cursor.fetchone()[0])

# Test sqlite3.Connection.create_aggregate
class Sum:
    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count

conn.create_aggregate('sum', 1, Sum)
