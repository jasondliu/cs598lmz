import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect():

# conn = sqlite3.connect("./test.db")
# cursor = conn.cursor()

# cursor.execute("create table user(id varchar(20) primary key, name varchar(20))")
# cursor.execute("insert into user(id, name) values(?, ?)", ("1", "jack"))
# cursor.execute("select * from user")
# values = cursor.fetchall()
# print(values)

# conn.commit()
# conn.close()

# Test sqlite3.Row():

# conn = sqlite3.connect("./test.db")
# cursor = conn.cursor()

# cursor.execute("create table user(id varchar(20) primary key, name varchar(20))")
# cursor.execute("insert into user(id, name) values(?, ?)", ("1", "jack"))
# cursor.execute("select * from user")

# values = cursor.fetchall()
# print(values)

# cursor.row_factory = sqlite3.Row

