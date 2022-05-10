import selectors
import json
import time
import random
import os
import sys

class Client:
    def __init__(self, host, port, nickname):
        self.host = host
        self.port = port
        self.nickname = nickname
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.sel = selectors.DefaultSelector()
        self.sel.register(self.socket, selectors.EVENT_READ, self.on_read)
        self.sel.register(sys.stdin, selectors.EVENT_READ, self.on_write)

    def on_read(self, conn, mask):
        try:
            data = conn.recv(1024)
        except ConnectionResetError:
            print('Server closed connection')
            self.sel.unregister(self.socket)
            self.socket.close()
            return
        if data:
            print(data.decode('utf8'))
        else:
            self.
