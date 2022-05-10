import socket
import time
import threading
from datetime import datetime
from time import sleep
import random
import os
import sys
import subprocess
import shutil
import re

#from multiprocessing import Process

class Server:
    def __init__(self):
        self.host = '192.168.1.4'
        self.port = 5555
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen(1)
        self.conn, self.addr = self.s.accept()
        print("Connection from: " + str(self.addr))
        self.start()

    def start(self):
        while True:
            data = self.conn.recv(1024).decode()
            if not data:
                break
            print("from connected  user: " + str(data))

            data = input("? ")
            self.conn.send(data.encode())

