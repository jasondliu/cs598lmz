import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('../data/weather.db')

# http://zetcode.com/db/sqlitepythontutorial/
# http://www.4programmers.net/Python/Python_operacje_na_bazie_danych_SQLite3

class db_thread(threading.Thread):
    def __init__(self, event, conn):
        threading.Thread.__init__(self)
        self.stopped = event
        self.conn = conn
        self.cursor = conn.cursor()
        #self.cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        #self.conn.commit()

