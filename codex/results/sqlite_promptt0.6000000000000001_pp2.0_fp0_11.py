import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
cursor.execute("insert into user (id, name) values ('1', 'Michael')")
print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()

# Test select

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("select * from user where id=?", ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

# Test Threading

# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(1000000):
#         lock.acquire()
#        
