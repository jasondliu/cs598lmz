import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table test(id integer primary key, name text)")
cur.execute("insert into test(name) values (?)", ("foo",))
cur.execute("insert into test(name) values (?)", ("bar",))
cur.execute("select id, name from test")

print(cur.fetchall())

cur.close()
conn.close()
# Test sqlite3.complete_statement()
sql = "select 1;"
print(sqlite3.complete_statement(sql))

sql = "select 1"
print(sqlite3.complete_statement(sql))

sql = "select 1;"
print(sqlite3.complete_statement(sql))

sql = "select 1;"
print(sqlite3.complete_statement(sql))

sql = "select 1;"
print(sqlite3.complete_statement(sql))
# Test sqlite3.register_converter()
def convert_int(s):
    return int(s)

