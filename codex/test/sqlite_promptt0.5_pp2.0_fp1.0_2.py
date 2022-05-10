import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:") to make sure it exists
import sqlite3

# Global variable
sqlite3.threadsafety = 1

# Import the database
try:
    db = sqlite3.connect('/home/pi/Desktop/Database/db.sqlite')
except sqlite3.Error:
    print("Error: database not found")
    exit(1)

# Import the database
try:
    db = sqlite3.connect('/home/pi/Desktop/Database/db.sqlite')
except sqlite3.Error:
    print("Error: database not found")
    exit(1)

# Import the database cursor
cursor = db.cursor()

# Import the database cursor
cursor = db.cursor()

# Import the database cursor
cursor = db.cursor()

# Import the database cursor
cursor = db.cursor()

# Import the database cursor
cursor = db.cursor()

# Import the database cursor
cursor = db.cursor()

# Import the database cursor
cursor = db.cursor()
