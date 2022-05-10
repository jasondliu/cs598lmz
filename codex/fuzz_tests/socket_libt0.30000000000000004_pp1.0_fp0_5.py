import socket
import sys
import time
import threading
import os
import random

class Client:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.socket.setblocking(0)
        self.socket.send(self.name.encode())
        self.socket.settimeout(0.1)
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()
        self.input_thread = threading.Thread(target=self.input_run)
        self.input_thread.start()

    def run(self):
        while self.running:
            try:
                data = self.socket.recv(1024)
                if data:
                    print(data.decode())
            except socket.timeout:
                pass
            except Connection
