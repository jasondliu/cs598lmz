import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('create table test(id integer, name varchar(255));')
cur.execute('insert into test (id, name) values (?, ?)', (1, 'test'))
conn.commit()
cur.execute('select * from test;')
print cur.fetchall()
cur.close()
conn.close()

# import subprocess
# print subprocess.Popen('ls', stdout=subprocess.PIPE).stdout.read()

# print globals()
print '\n'.join(threading.enumerate())

cc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
def set_maxfd(mf):
    cc.sysconf('sc_open_max')
    cc.setrlimit(ctypes.c_int(7), (
