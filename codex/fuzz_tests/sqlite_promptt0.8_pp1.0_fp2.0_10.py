import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
con = sqlite3.connect("test.db")
con.isolation_level = None
cur = con.cursor()

# Create a Table
def create_table():
    cur.execute("CREATE TABLE table3 (id INT, name TEXT, price INT)")

# Insert a row of data
def insert_data():
    cur.execute("INSERT INTO table3 VALUES (1, 'Apple', 100)")
    cur.execute("INSERT INTO table3 VALUES (2, 'Orange', 50)")
    cur.execute("INSERT INTO table3 VALUES (3, 'Grape', 20)")
    cur.execute("INSERT INTO table3 VALUES (4, 'Melon', 60)")

# Select Data
def select_data():
    cur.execute("SELECT * FROM table3")
    # fetch data in all rows
    res = cur.fetchall()
    print(res)

# exec_data()
create_table()
insert_data()
select_data()
