import socket
import sys
import time

from . import utils
from .config import Config
from .log import Log


class Client(object):
    """
    Client for the remote host.
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.sock.connect((self.host, self.port))
        self.sock.settimeout(1)
        self.log = Log()
        self.config = Config()

    def send(self, command):
        """
        Send command to the remote host.
        """
        self.sock.sendall(command.encode())
        self.log.debug('Sending command: %s' % command)

    def receive(self):
        """
        Receive data from the remote host.
       
