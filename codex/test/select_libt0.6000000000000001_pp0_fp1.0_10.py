import selectors
import socket
import sys
import types

from server.log import logger
from server.config import HOST, PORT
from server.event_handler import EventHandler


class Server:
    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.event_handler = EventHandler(self.sel)
        self.host = HOST
        self.port = PORT
        self.sock = socket.socket()
        self.sock.bind((self.host, self.port))
        self.sock.listen()
        self.sock.setblocking(False)
        self.sel.register(self.sock, selectors.EVENT_READ, self.event_handler.accept)

    def run(self):
        try:
            while True:
                events = self.sel.select()
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj, mask)
        except KeyboardInterrupt:
            logger.info("caught keyboard interrupt, exiting...")
