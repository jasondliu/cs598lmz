import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect('./data/test.db')
# c = conn.cursor()
# sql = "create table test (a varchar(10))"
# c.execute(sql)
# sql = "insert into test (a) values ('hello')"
# c.execute(sql)
# conn.commit()
# c.close()
conn = sqlite3.connect('./data/test.db')
c = conn.cursor()
sql = "select * from test"
c.execute(sql)
values = c.fetchall()
print(values)

sql = "insert into test (a) values ('hello')"
c.execute(sql)
conn.commit()
sql = "select * from test"
c.execute(sql)
values = c.fetchall()
print(values)

sql = "update test set a='world' where a='hello'"
c.execute(sql)
conn.commit()
sql = "select * from test"
c.execute(sql)
values = c.fetchall()
