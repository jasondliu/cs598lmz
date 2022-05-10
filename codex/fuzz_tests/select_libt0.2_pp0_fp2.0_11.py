import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import control
from . import crypto
from . import daemon
from . import event
from . import log
from . import network_util
from . import packet
from . import path
from . import process
from . import protocol
from . import util

_logger = log.get_logger(__name__)


class _Client(object):
    """A client connection to a server."""

    def __init__(self, server, sock, addr):
        self.server = server
        self.sock = sock
        self.addr = addr
        self.protocol = protocol.Protocol(sock)
        self.last_activity = time.time()
        self.is_authenticated = False
        self.is_authorized = False
        self.is_closed = False
        self.is_closing = False
        self.is_idle = False
        self.is_idle_timeout = False
        self.is
