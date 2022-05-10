import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#db = sqlite3.connect('database.db')
#db.execute('create table test (id INTEGER PRIMARY KEY, name TEXT)')
#db.execute('insert into test (name) values (?)', ('name',))
#db.commit()
#print db.execute('select * from test').fetchall()
#db.close()

#Test ctypes
#lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
#print lib
#print dir(lib)
#print lib.printf('Hello, %s\n', 'world')

#Test ctypes.util.find_library
#lib = ctypes.util.find_library('c')
#print lib
#lib2 = ctypes.util.find_library('m')
#print lib2
#print ctypes.util.find_library('pthread')

#Test threading
#class MyThread(threading.Thread):
#    def __init__(self, id):
#        threading.Thread.__init__(self)

