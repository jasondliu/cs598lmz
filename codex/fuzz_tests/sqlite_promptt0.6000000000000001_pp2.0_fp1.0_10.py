import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
dbPath = 'db'
db = sqlite3.connect(dbPath)

# Create a cursor object
cursor = db.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                userid INTEGER PRIMARY KEY,
                username TEXT,
                email TEXT,
                password TEXT)''')

# Insert data
cursor.execute('''INSERT INTO user (username, email, password) 
                VALUES ('test', 'test@gmail.com', '123456')''')
db.commit()

# Insert data
cursor.execute('''INSERT INTO user (username, email, password) 
                VALUES ('test2', 'test2@gmail.com', '123456')''')
db.commit()

# Read data
cursor.execute('''SELECT * FROM user''')
result = cursor.fetchall()
print(result)

# Close db
db.close()

# Test sqlite3.connect()
dbPath = 'db'
db = sqlite
