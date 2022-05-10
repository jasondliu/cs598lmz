import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
try:
    cursor.execute("create table person(id varchar(20) primary key, name varchar(20), score int)")
    cursor.execute("insert into person values('A-001', 'Adam', 95)")
    cursor.execute("insert into person values('A-002', 'Bart', 62)")
    cursor.execute("insert into person values('A-003', 'Lisa', 78)")
    cursor.execute("select * from person where id = 'A-002'")
    values = cursor.fetchall()
    print(values)
finally:
    cursor.close()
    conn.commit()
    conn.close()

print("----------")

# Test threading
balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(100000):
        lock.acquire()
