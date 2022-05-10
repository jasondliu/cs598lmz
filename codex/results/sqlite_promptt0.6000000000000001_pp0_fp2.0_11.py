import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
try:
    conn = sqlite3.connect('test.db')
    print('Success to connect')
except:
    print('Fail to connect')

cursor = conn.cursor()

cursor.execute('CREATE TABLE user (id varchar(20) primary key, name varchar(20))')

cursor.execute('INSERT INTO user (id, name) values (\'1\', \'Michael\')')

print(cursor.rowcount)

cursor.close()

conn.commit()
conn.close()

# Test threading
# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 先
