import select
import socket
import sys

from server.utils import (
    read_until,
    write_all,
)

class Server(object):

    def __init__(self, port, key):
        self.port = port
        self.key = key
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', port))
        self.sock.listen(5)
        self.clients = {}

