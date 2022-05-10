import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Create a database in RAM
db = sqlite3.connect(':memory:')

# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('mydb')

# Get a cursor object
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                       phone TEXT, email TEXT unique, password TEXT)
''')
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES('Andres', '3366858', 'user@example.com', '12345')''')
db.commit()

db.close()

# Test sqlite3.Cursor.execute()

db = sqlite3.connect('mydb')
cursor = db.cursor()
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES('John', '5557241', 'johndoe@example.com', 'johndoe123')''')
