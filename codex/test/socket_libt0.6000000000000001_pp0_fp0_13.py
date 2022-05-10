import socket
import threading
import time
import sys

class Client(threading.Thread):
    def __init__(self, _id, _name, _conn, _addr):
        threading.Thread.__init__(self)
        self.id = _id
        self.name = _name
        self.conn = _conn
        self.addr = _addr
