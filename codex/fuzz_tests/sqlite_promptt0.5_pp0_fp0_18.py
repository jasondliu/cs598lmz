import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/Users/huangjian/Desktop/test.db")

class Net:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect("/Users/huangjian/Desktop/test.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS ip_mac_table (
                            id INTEGER PRIMARY KEY,
                            ip TEXT,
                            mac TEXT
                            )""")
        self.conn.commit()

    def get_mac_by_ip(self, ip):
        self.cursor.execute("SELECT * FROM ip_mac_table WHERE ip=?", (ip,))
        mac = self.cursor.fetchone()
        if mac:
            return mac[2]
        else:
            return None

    def get_ip_by_mac(self, mac):
        self.cursor.execute("SELECT * FROM ip_mac_table WHERE mac=?", (mac,))
        ip
