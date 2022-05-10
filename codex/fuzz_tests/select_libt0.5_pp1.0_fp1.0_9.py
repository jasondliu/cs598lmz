import select
import socket
import sys
import threading
import time
import traceback

import cv2
import numpy as np

from cv2 import cv2

from src.server.utils import pack_message
from src.server.utils import unpack_message

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = {}
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.sock.setblocking(0)
        self.thread = threading.Thread(target=self.run)

    def run(self):
        print('Server started')
        while True:
            try:
                client, address = self.sock.accept()
                print('Connected with ' + address[0] + ':' + str(address[1]))
                client.setblocking(0
