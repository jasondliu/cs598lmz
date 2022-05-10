import socket
import sys
import time

from . import constants
from . import exceptions
from . import util
from . import wire

def _is_ssl(sock):
    return hasattr(sock, 'cipher')

class Socket(object):
    def __init__(self, sock, addr, debug=False):
        self.sock = sock
        self.addr = addr
        self.debug = debug
        self.is_ssl = _is_ssl(sock)
        self.is_closed = False
        self.is_broken = False
        self.is_read_ready = False
        self.is_write_ready = False
        self.is_read_closed = False
        self.is_write_closed = False

        self.read_buffer = bytearray()
        self.write_buffer = bytearray()

    def __repr__(self):
        return '<Socket at %#x: %s %s>' % (id(self), self.addr, self.sock)

    def __str__(self):
        return
