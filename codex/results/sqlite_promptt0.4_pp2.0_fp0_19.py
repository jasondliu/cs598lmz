import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# create table
def create_table():
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    sql = "create table company(id int primary key, name text not null, age int not null, address char(50), salary real)"
    cursor.execute(sql)
    connection.commit()
    connection.close()

# insert data
def insert_data():
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    sql = "insert into company(id, name, age, address, salary) values(1, 'Paul', 32, 'California', 20000.00 )"
    cursor.execute(sql)
    connection.commit()
    connection.close()

# select data
def select_data():
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    sql = "select * from company"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    connection.close()

#
