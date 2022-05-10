import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections

# Clean up old database if it exists
try:
	os.unlink('test.db')
except IOError:
	pass

# Test creating, opening and closing a database
conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.close()
conn.close()

# Test creating and opening a database
conn = sqlite3.connect('test.db')
cur = conn.cursor()

# Test table creation
cur.execute('CREATE TABLE Test (id integer primary key, val text)')

# Test insertion
cur.execute('INSERT INTO Test (id, val) VALUES (1, "a")')
cur.execute('INSERT INTO Test (id, val) VALUES (2, "b")')

# Test retrieval
cur.execute('SELECT * FROM Test')
print cur.fetchall()

# Test deletion, insertion, and updating
cur.execute('DELETE FROM Test')
cur.execute('INSERT INTO Test (id, val) VALU
