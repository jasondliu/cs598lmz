import select
import socket
import time

from . import util
from . import config
from . import log

class Server(object):
    def __init__(self, config):
        self.config = config
        self.log = log.Log(config)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.config.server_host, self.config.server_port))
        self.server_socket.listen(5)
        self.server_socket.setblocking(0)

        self.clients = {}
        self.client_count = 0

        self.log.info("Server started on %s:%s" % (self.config.server_host, self.config.server_port))

    def run(self):
        while True:
            self.tick()
            time.sleep(0.01)

    def tick(
