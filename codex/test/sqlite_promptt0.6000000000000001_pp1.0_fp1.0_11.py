import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('test.db')

# db = sqlite3.connect(':memory:')
db = sqlite3.connect('test.db')

def initDB():
    db.execute('''CREATE TABLE IF NOT EXISTS users
                 (userID INTEGER PRIMARY KEY, userName TEXT UNIQUE, password TEXT, email TEXT, phone TEXT, address TEXT, created_at TEXT)''')
    db.execute('''CREATE TABLE IF NOT EXISTS products
                 (productID INTEGER PRIMARY KEY, productName TEXT, price REAL, created_at TEXT)''')
    db.execute('''CREATE TABLE IF NOT EXISTS orders
                 (orderID INTEGER PRIMARY KEY, userID INTEGER, productID INTEGER, quantity INTEGER, created_at TEXT)''')
    db.commit()

