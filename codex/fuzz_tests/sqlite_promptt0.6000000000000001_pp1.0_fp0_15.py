import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# import sqlite3
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# c.execute("create table test (x integer, y integer)")
# c.execute("insert into test values (1,2)")
# c.execute("insert into test values (2,3)")
# c.execute("insert into test values (3,1)")
# c.execute("insert into test values (4,5)")
# c.execute("insert into test values (5,6)")
# c.execute("insert into test values (6,4)")
# conn.commit()
# conn.close()

def test():
    print("hello world")
    print("hello world again")
    return

def t1():
    global x
    x = 10
    print("t1 x: " + str(x))
    return

def t2():
    global x
    x = 20
    print("t2 x: " + str(x))
    return

def t3():
    global x
    x =
