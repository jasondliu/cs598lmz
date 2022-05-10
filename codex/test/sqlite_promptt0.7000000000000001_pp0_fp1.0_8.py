import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
# Test sqlite3.Cursor
cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, value TEXT)")
cursor.execute("INSERT INTO test (value) VALUES (?)", ("some data",))
cursor.execute("SELECT id, value FROM test")
(id, value) = cursor.fetchone()
print("id: %s, value: %s" % (id, value))
# Test sqlite3.Row
cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, value TEXT)")
cursor.execute("INSERT INTO test (value) VALUES (?)", ("some data",))
cursor.execute("SELECT id, value FROM test")
row = cursor.fetchone()
print("id: %s, value: %s" % (row[0], row[1]))
print("id: %s, value: %s" % (row["id"], row["value"]))
# Test sqlite3.
