import select
import socket
import sys
import threading
import time

import pykka


class Server(pykka.ThreadingActor):
    def __init__(self, port, handler_class):
        super(Server, self).__init__()
        self.port = port
        self.handler_class = handler_class
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(('', self.port))
        self.s.listen(5)
        self.s.setblocking(0)
    def on_start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()
    def run(self):
        while True:
            try:
                r, w, e = select.select([self.s], [], [], 5)
                if self.
