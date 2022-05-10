import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()


# 创建持久连接，默认文件不锁定，如果指定check_same_thread=False则也不会锁定文件，但是多线程访问会有问题，会出现OperationalError: database is locked错误
# 如果check_same_thread=True则在初始化时会锁定文件，在线程中共享是不会有问题的
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
with open('test.db', 'w') as f:
    pass
# 这样创建的连接是transient的，关
