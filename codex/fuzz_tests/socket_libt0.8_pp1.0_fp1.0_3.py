import socket
import errno
import select
from util import *

logger = logging.getLogger("tcp_server")


class Server:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        self.sock.bind((self.address, self.port))
        self.sock.listen(self.backlog)
        logger.info("Listening on %s.", self.sock.getsockname())
        self.running = True
        self.clients = {}
        self.recv_buffer = {}
        self.send_buffer = {}
        try:
            while self.running:
                rlist, wlist, xlist = select.select(self.get_all_
