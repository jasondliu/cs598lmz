import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, value TEXT)")
c.execute("INSERT INTO test VALUES (1, 'test')")
c.execute("SELECT * FROM test")
print(c.fetchone())
conn.close()

# Test sqlite3.connect() with timeout
conn = sqlite3.connect(":memory:", timeout=1)
c = conn.cursor()
c.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, value TEXT)")
c.execute("INSERT INTO test VALUES (1, 'test')")
c.execute("SELECT * FROM test")
print(c.fetchone())
conn.close()

# Test sqlite3.connect() with isolation_level
conn = sqlite3.connect(":memory:", isolation_level="EXCLUSIVE")
c = conn.cursor()
c.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, value TEXT)")
