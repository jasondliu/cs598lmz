import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# 1. Open a connection
conn = sqlite3.connect('test.db')

# 2. Create a cursor
cur = conn.cursor()

# 3. Execute a query
cur.execute("SELECT * FROM user")

# 4. Fetch the result
print(cur.fetchall())

# 5. Close the connection
conn.close()

# Test sqlite3.connect()

# 1. Open a connection
conn = sqlite3.connect('test.db')

# 2. Create a cursor
cur = conn.cursor()

# 3. Execute a query
cur.execute("SELECT * FROM user")

# 4. Fetch the result
print(cur.fetchall())

# 5. Close the connection
conn.close()
# Test sqlite3.connect()

# 1. Open a connection
conn = sqlite3.connect('test.db')

# 2. Create a cursor
cur = conn.cursor()

# 3. Execute a query
cur.execute("SELECT * FROM user")

# 4.
