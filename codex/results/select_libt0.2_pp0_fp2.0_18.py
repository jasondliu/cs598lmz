import select
import socket
import sys
import time
import traceback

from . import config
from . import log
from . import util
from . import xlog
from . import xlogviewer
from . import xlogviewer_pb2

class XlogViewerServer(object):
    def __init__(self, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', self.port))
        self.sock.listen(1)
        self.sock.setblocking(0)
        self.connections = {}

    def run(self):
        while True:
            try:
                self.handle_connections()
            except KeyboardInterrupt:
                break
            except:
                traceback.print_exc()

    def handle_connections(self):
        rlist, wlist, xlist
