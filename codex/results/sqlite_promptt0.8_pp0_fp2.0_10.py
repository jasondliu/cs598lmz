import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(":memory:")
curs = conn.cursor()
curs.execute("create table test(i int, s text)")
curs.execute("insert into test(i, s) values (1, 'hello world')")
curs.execute("select i, s from test")
print(curs.fetchall())
conn.close()

print(sqlite3.sqlite_version, sqlite3.version)

# Test libsqlite3.so
cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))

# Test sqlite3.connect()
conn = sqlite3.connect(":memory:")
curs = conn.cursor()
curs.execute("create table test(i int, s text)")
curs.execute("select i, s from test")
curs.fetchall()


# Test threading
def worker(lock, d):
    lock.acquire()
    d['cnt'] += 1
    lock.release()

d = {'cnt': 0
