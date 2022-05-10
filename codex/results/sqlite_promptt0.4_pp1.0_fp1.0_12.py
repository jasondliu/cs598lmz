import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
db = sqlite3.connect("/home/pi/sqlite/test.db")
cursor = db.cursor()
cursor.execute("SELECT * FROM test")
print(cursor.fetchall())
db.close()

# Test sqlite3.connect()
db = sqlite3.connect("/home/pi/sqlite/test.db")
cursor = db.cursor()
cursor.execute("SELECT * FROM test")
print(cursor.fetchall())
db.close()

# Test sqlite3.connect()
db = sqlite3.connect("/home/pi/sqlite/test.db")
cursor = db.cursor()
cursor.execute("SELECT * FROM test")
print(cursor.fetchall())
db.close()

# Test sqlite3.connect()
db = sqlite3.connect("/home/pi/sqlite/test.db")
cursor = db.cursor()
cursor.execute("SELECT * FROM test")
print(cursor.fetchall())
db.close()
