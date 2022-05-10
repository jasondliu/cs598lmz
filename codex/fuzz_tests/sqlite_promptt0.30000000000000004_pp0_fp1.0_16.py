import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Create a database in RAM
db = sqlite3.connect(':memory:')
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
db.commit()

name1 = 'Andres'
phone1 = '3366858'
email1 = 'user@example.com'
# A very secure password
password1 = '12345'

name2 = 'John'
phone2 = '5557241'
email2 = 'johndoe@example.com'
password2 = 'abcdef'

# Insert user 1
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''',
