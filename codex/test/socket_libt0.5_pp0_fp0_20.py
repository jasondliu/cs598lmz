import socket
import sys
import os
import time
import re
import subprocess
import threading
import logging

from logger import Logger
from utils import Utils
from config import Config

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)
        self.logger = Logger()
        self.utils = Utils()
        self.config = Config()

    def connect(self):
        self.logger.write("Connecting to server on port " + str(self.port))
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        return self.sock

    def receive(self):
        while True:
            data = self.sock.recv(4096)
            if not data:
                break
            print(data)

    def send(self, data):
        self.sock.send(data)
        return self.sock

   
