import select
import time
from datetime import datetime
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

class Message:
    def __init__(self, message, sender):
        self.message = message
        self.sender = sender
        self.time = datetime.now()

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.messages = []
        self.clients = []
        self.sockets = []

    def run(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        self.sockets.append
