import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#import sqlite3
#sqlite_file = '/home/dante/testsqlite.db'    # name of the sqlite database file
#conn = sqlite3.connect(sqlite_file)
#c = conn.cursor()
#c.execute('CREATE TABLE mytable (anything text)')
#conn.commit()
#conn.close()

# Test MySQL
#import mysql.connector
#cnx = mysql.connector.connect(user='dante', password='dante',
#                              host='10.0.2.2',
#                              database='mydb')
#cnx.close()



class HIDReport(object):
    def __init__(self, report_id=0, report_type=1, data=None):
        self.report_id = report_id & 0xFF
        self.report_type = report_type
        if data is None:
            data = []
        self.data = data

    def __str__(self):
        return "[Report %d %s] %s" % (self
