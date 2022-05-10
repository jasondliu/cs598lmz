import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Create a table
def create_table(conn):
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    conn.commit()

# Insert a row of data
def insert_stock(conn):
    c = conn.cursor()

    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    conn.commit()

# Print all the rows in the table
def print_stocks(conn):
    c = conn.cursor()

    # Do this instead
    t = ('RHAT',)
    c.execute('SELECT * FROM stocks WHERE symbol=?', t
