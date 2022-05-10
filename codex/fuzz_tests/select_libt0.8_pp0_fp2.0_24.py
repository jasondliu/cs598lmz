import select
import socket

from util import *

class Server(object):
    """
    Server is a class for creating and managing a server.
    """
    def __init__(self, hostname, port, channel):
        """Initialization

        Args:
            hostname (str): the hostname of the Server
            port (int): the port of the Server
            channel (str): the channel of the Server
        """
        self.hostname = hostname
        self.port = int(port)
        self.channel = channel
        self.clients = set()

    def start(self):
        """
        Start a server listening on the port and hostname passed during
        initialization.

        Returns:
            None
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.hostname, self.port))
        sock.listen(5)
        sock.setblocking(False)

        self.sock = sock
        self.selector = select.select([sock], [], [], 0
