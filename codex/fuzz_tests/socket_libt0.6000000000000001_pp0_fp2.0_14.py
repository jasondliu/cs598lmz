import socket
import threading
import json
import time
import sys

from lib.logger import *
import lib.settings as settings

class Server:
    def __init__(self, ip=settings.IP, port=settings.PORT):
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.ip, self.port))
        self.s.listen(10)
        self.s.settimeout(0.2)
        self.connections = []
        self.peers = []

    def handler(self, c, a):
        while True:
            try:
                data = c.recv(1024)
                for connection in self.connections:
                    try:
                        connection.send(data)
                    except:
                        self.connections.remove(connection)
                if not data:

