import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() function

# create a connection object
conn = sqlite3.connect('test.db')

# create a cursor object
cursor = conn.cursor()

# execute SQL statement
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# insert a record
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

# get the number of affected rows
print(cursor.rowcount)

# close cursor
cursor.close()

# commit
conn.commit()

# close connection
conn.close()

# Test sqlite3.cursor() function

# create a connection object
conn = sqlite3.connect('test.db')

# create a cursor object
cursor = conn.cursor()

# execute SQL statement
cursor.execute('select * from user where id=?', ('1',))

# get the result set
values = cursor.fetchall()
print(values)

# close cursor
cursor.close
