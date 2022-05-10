import ctypes
import ctypes.util
import threading
import sqlite3
import struct

try:
    import c_icap
except ImportError:
    print("Please setup the ctypes module and c-icap library properly")
    exit(1)

class CIcapError(Exception):
    pass


#We recomend to use multiple threads to handle multiple clients
#and  multiple yara rules.
#The simplest way is to implement a thread for each client.
class ScanRequestHandler(threading.Thread):
    PREVIEW_SIZE = 2048 #2Kb

    def __init__(self,conn,server,yara_rules,yara_timeout=10):
        threading.Thread.__init__(self)
        self.yara_rules = yara_rules
        self.yara_timeout = yara_timeout
        self.conn = conn
        self.server = server

