import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# connect = sqlite3.connect(":memory:")
# cursor = connect.cursor()
# cursor.execute("create table test(id smallint primary key, data text)")
# cursor.execute("insert into test(id, data) values (?, ?)", (1, "test"))
# connect.commit()
# cursor.execute("select data from test")
# print(cursor.fetchall())
# connect.close()
# ======================
# Python Call library functions
# gethostbyname = ctypes.CDLL(ctypes.util.find_library("c")).gethostbyname
# print(gethostbyname("yahoo.co.jp"))
# =======================
# Python SQLite3 database
# make connection to SQLite show database
# connect database = sqlite3.connect("test_database.db")
# connect database = sqlite3.connect("")
# make cursor to execute database function
# database_cursor = database.cursor()
# execute database with SQL command
# database_cursor.execute("select * from test_table")
# get result of database connection
