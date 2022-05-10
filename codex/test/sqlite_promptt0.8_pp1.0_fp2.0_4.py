import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() method
# if the database is not there, it creates a new database
conn = sqlite3.connect('stock.db')
