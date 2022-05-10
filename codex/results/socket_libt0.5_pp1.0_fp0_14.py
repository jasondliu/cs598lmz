import socket
import time
import threading
from random import randint

class udp_client():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(10)

    def send(self, message):
        try:
            self.sock.sendto(message, (self.host, self.port))
            data, addr = self.sock.recvfrom(1024)
        except socket.timeout:
            print "socket timeout"
            return 0
        except socket.error, e:
            print "socket error: %s" % e
            return 0
        return data


class udp_server():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind
