import weakref
from functools import wraps
from contextlib import contextmanager, closing
from collections import defaultdict
from twisted.internet.defer import Deferred
from twisted.internet.protocol import ServerFactory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.protocols.ftp import FTPFactory, FTPRealm, Authorizer
from twisted.cred.portal import Portal

class Server(object):
    """
    Thing that owns the FTPD factory and can be started and stopped.
    """
    def __init__(self, controller=None, addr="127.0.0.1", port=2121, passive_ports=[12345]):
        self.controller = controller
        self.addr = addr
        self.port = port
        self.passive_ports = passive_ports

        self._factory = None
        if not controller.filesystem:
            controller.filesystem = Filesystem()
        self.filesystem = controller.filesystem

        self.realm = FTPRealm()

        # the default Authorizer doesn't supply a writeable temporary
        #
