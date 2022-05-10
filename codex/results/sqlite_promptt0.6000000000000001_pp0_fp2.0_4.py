import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# import sqlite3
# conn = sqlite3.connect('/Users/jerry/Desktop/test.db')
# cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# print(cursor.rowcount)
# cursor.close()
# conn.commit()
# conn.close()

# 测试线程
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread
