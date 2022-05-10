import ctypes
ctypes.windll.user32.LockWorkStation()

import socket
import threading
import fcntl
import struct
import os
import time
import subprocess

HOST = '0.0.0.0'
PORT = 25001

HTTPROOT = 'http'

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

class RequestThread(threading.Thread):
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        
        super(RequestThread, self).__init__()
        
    def run(self):
        data = self.conn.recv(1024)
        print data
        
        # request type is auto-detected
