import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections()
# Test sqlite3.create_function()
# Test sqlite3.Row

db = sqlite3.connect(":memory:")

cursor = db.cursor()

cursor.execute("CREATE TABLE test (id integer PRIMARY KEY, name VARCHAR(20))")

cursor.execute("INSERT INTO test (name) VALUES (?)", ("pysqlite",))

cursor.execute("SELECT * FROM test")

row = cursor.fetchone()

print row

############################################################################

db = sqlite3.connect(":memory:")

cursor = db.cursor()

cursor.execute("CREATE TABLE test (id integer PRIMARY KEY, name VARCHAR(20))")

cursor.executemany("INSERT INTO test (name) VALUES (?)", (("pysqlite",), ("otherdb",)))

cursor.execute("SELECT * FROM test")

print cursor.fetchall()

############################################################################

db = sqlite3.connect(":memory
