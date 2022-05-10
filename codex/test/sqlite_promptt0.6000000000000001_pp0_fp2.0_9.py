import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
db = sqlite3.connect(':memory:')

# Create table
# db.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, data TEXT)')
# Insert data
db.execute('INSERT INTO test (data) VALUES (?)', ('Hello World!',))

# Save changes
db.commit()

# Read data
