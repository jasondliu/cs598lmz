import select
import socket
import sys

from util import get_logger

logger = get_logger('server_socket')

class ServerSocket(object):
    """
    Socket server
    """

    def __init__(self, host, port):
        """
        Initialize the socket server
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((host, port))
        self.socket.listen(5)
        self.inputs = [self.socket]
        self.outputs = []
        self.message_queues = {}

    def start(self):
        """
        Start the socket server
        """
        while True:
            readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs)
            for s in readable:
                if s is self.socket:
                    conn, addr =
