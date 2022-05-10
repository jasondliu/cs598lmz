import socket

from datetime import datetime
from random import randint
from threading import Thread

from utils.logger import Logger
from utils.data_utils import DataUtils
from utils.network_utils import NetworkUtils

class Server:
    def __init__(self, port=8080):
        self.host = NetworkUtils.get_host_ip()
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.logger = Logger()
        self.data_utils = DataUtils()

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
