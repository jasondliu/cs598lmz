import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
connection = sqlite3.connect("test.db")
cursor = connection.cursor()
cursor.execute("select * from test")
print cursor.fetchall()
connection.close()

# Test sqlite3.connect(":memory:")
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("select * from test")
print cursor.fetchall()
connection.close()

# Test sqlite3.connect("")
connection = sqlite3.connect("")
cursor = connection.cursor()
cursor.execute("select * from test")
print cursor.fetchall()
connection.close()

# Test sqlite3.connect("", uri=true)
connection = sqlite3.connect("", uri=True)
cursor = connection.cursor()
cursor.execute("select * from test")
print cursor.fetchall()
connection.close()

# Test sqlite3.connect("", uri=false)
connection = sqlite3.connect("", uri=False
