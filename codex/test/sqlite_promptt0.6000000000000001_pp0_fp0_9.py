import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/Users/zhanglijun/Desktop/test.db")
import time

def load_lib(name):
    path = ctypes.util.find_library(name)
    return ctypes.CDLL(path)

def init_db():
    conn = sqlite3.connect("/Users/zhanglijun/Desktop/test.db")
    cursor = conn.cursor()
    cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
    cursor.execute("insert into user (id, name) values ('1', 'Michael')")
    print(cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()

def query_db():
    conn = sqlite3.connect("/Users/zhanglijun/Desktop/test.db")
    cursor = conn.cursor()
    cursor.execute("select * from user where id=?", ('1',))
    values = cursor.fetchall()
    print(values)
    cursor.close()

