import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')


class DBService(threading.Thread):
    def __init__(self, sock, addr):
        threading.Thread.__init__(self)
        self.sock = sock
        self.addr = addr
        self.stop = False

