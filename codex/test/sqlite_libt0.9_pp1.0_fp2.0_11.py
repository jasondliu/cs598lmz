import ctypes
import ctypes.util
import threading
import sqlite3
import time
import re
import io

def ipv46str(ip):
    "convert 32-bit integer to dotted quad string"
    assert isinstance(ip, (int, long))
    import socket
    import struct
    return socket.inet_ntop(socket.AF_INET, struct.pack('>I', ip))

class DnsSnooperInterface(object):
    def log_event(self, data):
        pass

    def log_reply(self, id, addr, prefix, data):
        pass

    def log_dns(self, data):
        pass

class DnsSnooperConcreteInterface(DnsSnooperInterface):
    def __init__(self, dbname):
        # makes an SQLite DB in memory
        self.conn = sqlite3.connect(dbname)

    def log_event(self, data): 
        "record events associated with this listener"
        cursor = self.conn.cursor()
        # E.g. evdata is (process id, "start", time), etc.
