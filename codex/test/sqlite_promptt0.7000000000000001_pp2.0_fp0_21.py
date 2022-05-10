import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print(cursor.rowcount)

cursor.close()

conn.commit()
conn.close()
import datetime
print(datetime.datetime.now())
print(datetime.datetime(year=2019, month=1, day=1))
print(datetime.datetime.now()+datetime.timedelta(days=1))
print(datetime.datetime.now()+datetime.timedelta(hours=10))
print(datetime.datetime.now()+datetime.timedelta(minutes=10))
print(datetime.datetime.now()+datetime.timedelta(seconds=10))
