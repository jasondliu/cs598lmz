import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection().backup method in separate thread.


class BackupTest(threading.Thread):
    def __init__(self, dbname, targetdb):
        threading.Thread.__init__(self)
        self.dbname = dbname
        self.targetdb = targetdb

    def run(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.target = sqlite3.connect(self.targetdb)

        self.cursor.execute("create table foo(x)")
        self.cursor.executemany("insert into foo values (?)",
            [(x,) for x in range(10)])
        self.cursor.execute("delete from foo where x = 3")
        self.cursor.execute("delete from foo where x > 5")
        self.conn.commit()

        print("REWIND", self.conn.backup("main", self.target, "main"))
        print("FULL", self.conn.backup("main", self.target, "main
