import select
import socket
import sys
import time
import traceback

from . import config
from . import log
from . import util

class Server(object):
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.sock.setblocking(0)

    def run(self):
        while True:
            try:
                self.run_once()
            except KeyboardInterrupt:
                break
            except:
                log.error(traceback.format_exc())

    def run_once(self):
        rlist, wlist, xlist = select.select([self.sock], [], [], 1
