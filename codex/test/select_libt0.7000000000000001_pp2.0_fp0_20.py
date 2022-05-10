import select
import socket

from .base import _BaseSocket
from .log import _LogSocket


class _ListenSocket(_BaseSocket):

    def __init__(self, port, socketclass, log_prefix=None):
        super().__init__(socketclass=socketclass)
        self.port = port
        if log_prefix is None:
            log_prefix = socketclass.__name__
        self.log_prefix = log_prefix
        self.log("Listening on port %d", self.port)

    def get_socket(self):
        sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP
        )
        sock.setblocking(0)
        sock.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR,
            1)  # for immediate restart
        sock.bind(("", self.port))
        sock.listen(128)
        return sock

