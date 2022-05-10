import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# connect to DB, DB will be created if not exist
conn = sqlite3.connect("db")
# create cursor
cursor = conn.cursor()
# create table test
cursor.execute("""create table if not exists test(
    id integer PRIMARY KEY,
    name text)
""")
# add record
cursor.execute("""insert into test(id, name) 
                  values(1, 'first')""")
# commit change
conn.commit()
# cursor close
cursor.close()
# close connection
conn.close()
# select
conn = sqlite3.connect("db")
# create cursor
cursor = conn.cursor()
# select
cursor.execute("""select * from test""")
# fetch data
print(cursor.fetchall())
# close connection
cursor.close()
conn.close()
# ues queue to share variables between multiple threads
queue = queue.Queue()
# add thread
def job1(num):
    
    for i in range(num):
# add variable
        queue.put(i
