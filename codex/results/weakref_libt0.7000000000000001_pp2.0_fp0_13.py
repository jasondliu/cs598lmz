import weakref

import logging
_log = logging.getLogger(__name__)

from . import protocol, util

class Client(protocol.Client):
    def __init__(self, sock, addr, protocol_factory=None, **kwargs):
        self.addr = addr
        protocol.Client.__init__(self, sock, protocol_factory, **kwargs)

class Server(protocol.Server):
    def __init__(self, sock=None, protocol_factory=None, **kwargs):
        protocol.Server.__init__(self, sock, protocol_factory, **kwargs)

    def _make_connection(self, s):
        self.sock = s
        return Client(s, addr=s.getpeername(), protocol_factory=self.protocol_factory, server=weakref.proxy(self))

    def __call__(self, sock, addr):
        return self._make_connection(sock)

class MulticastServer(Server):
    def __init__(self, sock=None, protocol_f
