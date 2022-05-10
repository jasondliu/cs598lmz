import socket
import sys
import time
import threading
import os
import json

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))
        self.sender = Sender(self.socket)
        self.receiver = Receiver(self.socket)
        self.sender.start()
        self.receiver.start()
        self.sender.join()
        self.receiver.join()

class Sender(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket

    def run(self):
        while True:
            msg = input("")
            if msg == "exit":
                self.socket.close()
                sys.exit()
            else:
                msg = msg.encode()
                self.socket.send
