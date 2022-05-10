import socket
import sys
import thread
import time
from socket import error as SocketError
import errno

def get_host_ip(): 
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        if s:
            s.close()
    return ip

def listener():
    while True:
        data, addr = c.recvfrom(1024) # buffer size is 1024 bytes
