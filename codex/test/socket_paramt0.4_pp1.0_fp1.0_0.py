import socket
socket.if_indextoname(1)

# 使用网络库
import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))

# 使用操作系统接口
import os
print(os.uname())

# 访问数据库
import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()

# 使用模块
import sys
print(sys.path)

# 安装第三方模块
