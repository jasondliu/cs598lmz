import socket
import sys
import time
from threading import Thread, Lock

from lib.config import Config
from lib.log import Log


class Server(Thread):
    def __init__(self, port, config, log):
        Thread.__init__(self)
        self.port = port
        self.config = config
        self.log = log

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', port))
        self.sock.listen(5)

        self.clients = []
        self.clients_lock = Lock()

    def run(self):
        self.log.add('Listening on port %d' % self.port)
        while True:
            client, address = self.sock.accept()
