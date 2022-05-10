import selectors
import re
import time
import logging
from time import strftime

logger = logging.getLogger()


class Server(object):
    def __init__(self, host, port):
        self.hostname = host
        self.port = port
        self.sel = selectors.DefaultSelector()
        self.keep_running = True

    def start(self):
        """Start the server"""
        print("Listening")
        self.sel.register(socket.socket(), selectors.EVENT_READ, data=None)
        while self.keep_running:
            try:
                events = self.sel.select(timeout=None)
                for key, mask in events:
                    s = key.fileobj
                    data = key.data
                    if mask & selectors.EVENT_READ:
                        if s is self.ssock:
                            self.accept_wrapper(s)
                        else:
                            self.service_connection(s, data)
            except Exception as e:
                print("Exception: ", e)

    def accept_wrapper(self
