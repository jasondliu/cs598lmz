import select
import socket
import sys
import time
from threading import Thread

from . import config
from . import log
from . import messages
from . import util

_logger = log.getLogger('peer')


class Peer(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = None
        self.in_buf = b''
        self.out_buf = b''
        self.connected = False

        self.last_seen = time.time()
        self.last_ping = 0

    def __str__(self):
        return '%s:%d' % (self.ip, self.port)

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, str(self))

    def __eq__(self, other):
        return self.ip == other.ip and self.port == other.port

    def __hash__(self):
        return hash((self.ip, self.
