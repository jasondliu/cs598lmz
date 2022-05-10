import selectors
import socket
import types

from . import logs

logger = logging.getLogger(__name__)
info, warn, err = (logger.info, logger.warning, logger.error,)


class Server:
    def __init__(self, host, port):
        self.selector = selectors.DefaultSelector()
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lsock.bind((host, port))
        lsock.listen()
        lsock.setblocking(False)
        self.selector.register(lsock, selectors.EVENT_READ, self.accept)

    def accept(self, sock, mask):
        conn, addr = sock.accept()
        conn.setblocking(False)
        self.selector.register(conn, selectors.EVENT_READ, self.read)

    def read(self, conn, mask):
        data =
