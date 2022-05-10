import select
import socket
import sys

from . import common
from . import connection

logger = logging.getLogger(__name__)

class Server(object):
    def __init__(self, address):
        self.address = address
        self.sock = None
        self.connections = {}

    def start(self):
        self.sock = common.create_listening_socket(self.address)
        while True:
            r, w, x = select.select([self.sock], [], [])
            if self.sock in r:
                conn, addr = self.sock.accept()
                logger.info("Connection from %s", addr)
                c = connection.Connection(conn)
                self.connections[c.id] = c
                c.start()

    def stop(self):
        self.sock.close()
        for c in self.connections.values():
            c.stop()
        self.connections = {}
