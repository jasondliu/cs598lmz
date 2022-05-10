import select
import socket
import sys
import threading
import time
import os
import getpass
import random
import re

class Client(threading.Thread):
    def __init__(self, port, host, username, password, workdir):
        threading.Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, int(port)))
        self.sock.setblocking(0)
        self._buf = ""
        self.username = username
        self.password = password
        self.workdir = workdir
        self.login()

    def send(self, msg):
        self.sock.send(msg)

