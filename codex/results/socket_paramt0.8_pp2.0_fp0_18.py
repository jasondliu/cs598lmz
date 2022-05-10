import socket
socket.if_indextoname(4)

print(os.getenv('username'))
print(os.getlogin())

# with open('test.txt', 'w') as f:
#     f.write('testing')
#     print(f.closed)
# print(f.closed)

import time
import datetime

# time.sleep(2)
# print(time.time())

# dt = datetime.datetime(2016, 7, 24)
# print(dt)

# dt = datetime.datetime.now()
# print(dt)
# print(dt.date())
# print(dt.time())

# delta = datetime.timedelta(days=100)
# print(dt + delta)

import sqlite3

# db = sqlite3.connect('test.db')
# db.execute('drop table if exists test')
# db.execute('create table test (t1 text, i1 int)')
# db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
# db.execute
