import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# connect to the database
def connect():
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    return conn

# create a table
def create_table():
    conn = connect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS
                user(id INTEGER PRIMARY KEY,
                     username TEXT,
                     password TEXT)''')
    conn.commit()
    conn.close()

# add a user
def add_user(username, password):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO user VALUES (NULL, ?, ?)", (username, password))
    conn.commit()
    conn.close()

# view all users
def view_all_users():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM user")
    rows = c.fetchall()
    conn.close()
    return rows
