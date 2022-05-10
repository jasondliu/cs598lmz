import weakref
import socket
import re
import time
import logging

from .exceptions import *
from .util import *

logger = logging.getLogger('threepio')


class ActorClient(object):
    def __init__(self, server, port, name, socket=None, **kwargs):
        self.name = name
        self.server = server
        self.port = port
        self.register_patterns(kwargs)
        self.connect(socket)

    def connect(self, socket=None):
        self.sock = socket or self.connect_socket()
        host, _ = self.sock.getsockname()
        self.host = socket.gethostbyname(host)
        self.register()

    def register_patterns(self, patterns):
        self.message_handlers = {}
        for key, func in patterns.items():
            r = re.compile(key)
            self.register_message_handler(r, func)

    def register_message_handler(self, regex, func):
        self.message_
