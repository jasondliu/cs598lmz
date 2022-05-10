import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
connection = sqlite3.connect("test.db")
cursor = connection.cursor()
cursor.execute("select * from test")
