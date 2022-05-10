import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
db = sqlite3.connect('test.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE user(id INTEGER PRIMARY KEY, name TEXT,
                       phone TEXT, email TEXT unique, password TEXT)
''')
db.commit()
id = '12345'
user = ('name', 'phone', 'email', 'password')
cursor.execute('''INSERT INTO user(id, name, phone, email, password)
                  VALUES(?,?,?,?,?)''', (id, user[0], user[1], user[2], user[3]))
print('First name:', cursor.fetchone()[0])

# Test sqlite3.connect()
db = sqlite3.connect('test.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE user(id INTEGER PRIMARY KEY, name TEXT,
                       phone TEXT, email TEXT unique, password TEXT)
''')
db.commit()
id = '12345'
user = ('name',
