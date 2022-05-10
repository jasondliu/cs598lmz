import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
db = sqlite3.connect('test.db')

# Run sql
cur = db.cursor()
cur.execute("SELECT * FROM test")
rows = cur.fetchall()
print(rows)

# Close
db.close()

# Open again
db = sqlite3.connect('test.db')

# Run sql
cur = db.cursor()
cur.execute("SELECT * FROM test")
rows = cur.fetchall()
print(rows)

# Close
db.close()
