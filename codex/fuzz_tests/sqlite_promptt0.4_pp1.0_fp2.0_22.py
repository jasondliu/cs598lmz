import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

# SQLite dll path
dll_path = ctypes.util.find_library('sqlite3')
print(dll_path)

# Load dll
dll = ctypes.CDLL(dll_path)

# SQLite version
version = ctypes.c_char_p()
dll.sqlite3_libversion(ctypes.byref(version))
print(version.value)

# Open database
conn = sqlite3.connect(':memory:')
print(conn)

# Create table
conn.execute('CREATE TABLE person (id integer primary key, name varchar(64))')

# Insert data
conn.execute('INSERT INTO person (name) VALUES (?)', ('Mike',))
conn.execute('INSERT INTO person (name) VALUES (?)', ('John',))
conn.execute('INSERT INTO person (name) VALUES (?)', ('David',))

# Query data
cursor = conn.execute('SELECT * FROM person')
for row in cursor:
    print(row)

# Close database
conn.close()


