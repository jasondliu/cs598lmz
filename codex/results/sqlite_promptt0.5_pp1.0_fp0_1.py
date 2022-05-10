import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Initialize the database
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS test(
		a integer,
		b integer,
		c integer
	)''')
conn.commit()

# Insert data into the database
c.execute('''INSERT INTO test VALUES(1, 2, 3)''')
conn.commit()

# Query data from the database
c.execute('''SELECT * FROM test''')
print(c.fetchall())

conn.close()

# Test ctypes.util.find_library()

print(ctypes.util.find_library('c'))

# Test ctypes.cdll.LoadLibrary()

libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
print(libc.printf)

# Test ctypes.CDLL()

libc = ctypes.CDLL(ctypes.util.find_library('c'))
print
