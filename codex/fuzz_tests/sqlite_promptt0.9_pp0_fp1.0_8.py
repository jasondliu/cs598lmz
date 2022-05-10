import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#testSQLiteFile = "testSQLite.db"
#testSQLiteConn = sqlite3.connect(testSQLiteFile)
#testSQLiteCurs = testSQLiteConn.cursor()
#testSQLiteCurs.execute('''CREATE TABLE teste (t1, t2)''')
#testSQLiteCurs.execute('''INSERT INTO teste VALUES(1, 'franco')''')
#testSQLiteCurs.execute('''CREATE TABLE teste2 (t1, t2)''')
#testSQLiteCurs.execute('''INSERT INTO teste2 VALUES(1, 'franco')''')
#testSQLiteCurs.execute('''INSERT INTO teste2 VALUES(2, 'Paulo')''')
#testSQLiteCurs.execute('''
#    SELECT t1, t2 FROM teste
#    JOIN teste2 ON teste.t1 = teste2.t1
#''')

#testSQLiteCurs.execute('''SELECT * FROM test
