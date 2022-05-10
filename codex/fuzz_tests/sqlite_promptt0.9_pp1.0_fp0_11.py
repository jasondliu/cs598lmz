import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection()
#http://blog.chinaunix.net/uid-20746955-id-3273250.html
#http://tech.kakao.com/2015/03/03/sqlite/
#http://tianxiangbing.org/sqlite-database-usage.html
#http://www.cnblogs.com/pabell/articles/3710815.html

a = [[1, 2, 3], [4, 5, 6]]
print a[0][0]

class Matcher(object):
    def __init__(self):
        self.sql_lock = threading.Lock()
        self.db = sqlite3.connect('./matcher_db.db')
        self.cursor = self.db.cursor()
        
        self.cursor.execute('''
        CREATE TABLE match_point (
        point_id    INTEGER PRIMARY KEY AUTOINCREMENT,
        point_index INTEGER NOT NULL,
        x           INTEGER NOT NULL,
        y           INTEGER NOT NULL)

