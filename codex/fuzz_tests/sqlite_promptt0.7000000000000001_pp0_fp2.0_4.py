import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# SQLite database path
sqlite_db_path = './test.db'

# Create table
conn = sqlite3.connect(sqlite_db_path)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print(cursor.rowcount)

cursor.close()

conn.commit()
conn.close()

# Check whether the table is created
conn = sqlite3.connect(sqlite_db_path)
cursor = conn.cursor()
cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall()
print(values)

# Test Thread local

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread
