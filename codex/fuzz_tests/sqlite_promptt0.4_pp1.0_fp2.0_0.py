import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# SQLite3 数据库
# 数据库文件是一个文件
# 数据库表是一个数据文件
# 数据库表中的一行就是一条记录

# 创建数据库表
# create table table_name (
#   column1 datatype,
#   column2 datatype,
#   column3 datatype,
#   .....
#   columnN datatype,
# );

# 创建表
# CREATE TABLE COMPANY(
#    ID INT PRIMARY KEY     NOT NULL,
#    NAME           TEXT    NOT NULL,
#    AGE            INT     NOT NULL,
#    ADDRESS        CHAR(50),
#    SALARY         REAL
# );

# 插入数据
# INSERT INTO COMPANY (
