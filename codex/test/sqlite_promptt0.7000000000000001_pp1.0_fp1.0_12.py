import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import sqlite3
conn = sqlite3.connect('/root/Documents/Test/ZeeArrow-master/Mysql.db')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
values
cursor.close()
conn.close()

#!/usr/bin/env python
# coding=
