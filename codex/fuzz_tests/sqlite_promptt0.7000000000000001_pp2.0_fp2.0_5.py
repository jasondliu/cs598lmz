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
print cursor.fetchall()

# Test ctypes.util.find_library()
libc = ctypes.CDLL(ctypes.util.find_library('c'))
print libc.time(None)

# Test threading.Lock()
lock = threading.Lock()
lock.acquire()
lock.release()

# Test ctypes.CDLL().memmove()
s = ctypes.create_string_buffer('Hello World')
libc.memmove(s, 'Goodbye', len('Goodbye'))
print repr(s.value)
