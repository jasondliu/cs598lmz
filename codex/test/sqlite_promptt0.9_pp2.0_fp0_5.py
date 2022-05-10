import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/dnh/data.txt")

class Agent (threading.Thread):

    def __init__ (self):
        threading.Thread.__init__(self)
        self.conn = sqlite3.connect("data.txt")
        self.cursor = self.conn.cursor()
        self.cursor.executescript("""
            CREATE TABLE IF NOT EXISTS IP(USER_ID TEXT PRIMARY KEY,
                PASSWORD TEXT,
                TIME TEXT,
                IP_NAME TEXT,
                MODE TEXT,
                IP TEXT);""")

        self.cursor.execute("SELECT COUNT(*) FROM IP")
        r = self.cursor.fetchall()
        print("Now there are "+str(r[0][0])+" records in database.")

    def run (self):
        """
        1. clean database
        2. loop for user input
        """
        self.clean_database()
        while True:
            if self.get_input():
                print("Successfully added one record.")
