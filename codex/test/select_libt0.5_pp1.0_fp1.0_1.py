import selectors
import sys

from src.message import Message
from src.logger import logger
from src.config import *

class Client:
    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.connections = {}

    def connect(self, host, port):
        server_addr = (host, port)
        print("starting connection to", server_addr)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(sock, events, data=None)
        self.connections[sock] = {
            'addr': server_addr,
            'inb': b"",
            'outb': b"",
        }
