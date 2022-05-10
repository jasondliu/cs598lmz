import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/run/user/1000/gvfs/sftp:host=192.168.1.210,user=root/home/root/Downloads/INF4300.db')
#sqlite3.connect(':memory:')
#sqlite3.connect('/run/user/1000/gvfs/sftp:host=192.168.1.210,user=root/home/root/Downloads/INF4300.db').cursor().execute('SELECT * FROM Movie').fetchall()

#conn = sqlite3.connect('/home/student/Documents/INF4300.db')
#conn = sqlite3.connect('/run/user/1000/gvfs/sftp:host=192.168.1.210,user=root/home/root/Downloads/INF4300.db')
#conn = sqlite3.connect('/home/student/Documents/INF4300.db')
conn = sqlite3.connect('/home/student/Desktop/INF4300.db')
conn.row_factory = sql
