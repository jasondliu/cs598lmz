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
print db.execute('SELECT data FROM test').fetchall()

# Cleanup
db.close()

# Test ctypes.util.find_library()
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Test threading.Lock()
lock = threading.Lock()

# Test ctypes.CDLL()
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Test ctypes.CDLL()
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Test ctypes.CDLL()
libc = ctypes.CDLL(ctypes.util.find_library('
