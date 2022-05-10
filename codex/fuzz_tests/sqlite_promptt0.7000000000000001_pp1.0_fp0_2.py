import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# 数据库文件
DB_FILE_PATH = 'test.db'


def save_to_db(x, y):
    # 连接数据库，如果文件不存在会自动在当前目录创建:
    conn = sqlite3.connect(DB_FILE_PATH)
    # 创建一个Cursor:
    cursor = conn.cursor()
    # 执行一条SQL语句，创建user表:
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 继续执行一条SQL语句，插入一条记录:
    cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

