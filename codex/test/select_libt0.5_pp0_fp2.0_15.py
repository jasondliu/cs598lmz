import select
import socket
import sys
import threading

from Queue import Queue

import config

log = logging.getLogger(__name__)

def _add_sock(sock, socks):
    socks.append(sock)
    sock.setblocking(False)

class _Server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socks = []
        self.queue = Queue()

        self.start()

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def join(self):
        self.thread.join()

    def run(self):
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock
