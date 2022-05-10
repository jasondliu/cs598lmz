import select
import socket
import sys
import threading
import time

from . import utils
from . import ssl
from . import exceptions
from . import constants
from . import log

from . import _ssl_wrap_socket

class _BaseSocket(object):
    def __init__(self, sock, timeout=None, source_address=None):
        self.timeout = timeout
        self.source_address = source_address

        if sock is None:
            self.sock = None
        else:
            self.sock = _ssl_wrap_socket(sock)

    def settimeout(self, timeout):
        self.timeout = timeout

    def gettimeout(self):
        return self.timeout

    def setblocking(self, flag):
        self.timeout = None if flag else 0

    def setsockopt(self, level, optname, value):
        self.sock.setsockopt(level, optname, value)

    def getsockopt(self, level, optname):
        return self.sock.getsockopt(level, optname)

   
