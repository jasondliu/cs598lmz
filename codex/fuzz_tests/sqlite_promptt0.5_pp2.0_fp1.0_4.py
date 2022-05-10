import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/joe/test.db")

# import time

# Create the database
conn = sqlite3.connect("/home/joe/test.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS test")
cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, data TEXT)")

cursor.execute("INSERT INTO test VALUES (NULL, 'Hello World')")

cursor.execute("INSERT INTO test VALUES (NULL, 'Hello World')")
cursor.execute("INSERT INTO test VALUES (NULL, 'Hello World')")
cursor.execute("INSERT INTO test VALUES (NULL, 'Hello World')")
cursor.execute("INSERT INTO test VALUES (NULL, 'Hello World')")
cursor.execute("INSERT INTO test VALUES (NULL, 'Hello World')")
cursor.execute("INSERT INTO test VALUES (NULL, 'Hello World')")
cursor.execute("INSERT INTO test VALUES (NULL, 'Hello World')")
cursor
