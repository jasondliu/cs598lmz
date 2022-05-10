import select
import socket
import time
import errno
import logging
import sys
from urllib.parse import urlparse

from . import config
from . import util
from . import transaction
from . import http_types
from . import http_parser
from . import http_util
from . import http_exceptions


log = logging.getLogger(__name__)


class ClientConnection:
    """
    A client connection.
    """
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.closed = False
        self.transaction = None
        self.parser = http_parser.HttpRequestParser()
        self.send_buffer = bytearray()

    def read(self):
        """
        Read data from the connection.
        """
        try:
            data = self.conn.recv(config.BUFFER_SIZE)
        except (socket.error, OSError) as e:
            if e.errno == errno.EAGAIN:
                return
            raise

