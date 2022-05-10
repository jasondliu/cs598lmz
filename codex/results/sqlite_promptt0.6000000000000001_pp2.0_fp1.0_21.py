import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/pi/Desktop/test.db")

class slider:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.state = 0
        self.status = 0
        self.IP = 0
        self.port = 0
        self.sock = 0
        self.sock_connected = False
        self.sock_last_state = -1
        self.lock = threading.Lock()

    def set_state(self, state):
        self.lock.acquire()
        self.state = state
        self.lock.release()

    def set_status(self, status):
        self.lock.acquire()
        self.status = status
        self.lock.release()

    def set_IP(self, IP):
        self.lock.acquire()
        self.IP = IP
        self.lock.release()

    def set_port(self, port):
        self.lock.acquire()
        self.port = port
        self.lock.release()


