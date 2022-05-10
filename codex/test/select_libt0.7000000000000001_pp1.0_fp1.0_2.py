import select

from collections import deque
from datetime import datetime
from logging import getLogger
from socket import socket, timeout, SHUT_WR
from threading import Thread, Event

from . import BaseServer, Connection, ConnectionClosed
from .. import exceptions, compat, config


class SelectConnection(Connection):
    """A connection that works with select.select()."""

    def __init__(self, client, server, socket_file, address):
        super(SelectConnection, self).__init__(client, server, socket_file, address)
        self._read_buffer = b""
        self._write_buffer = deque()
        self._read_buffer_size = config.RECV_SIZE
        self._write_buffer_size = config.SEND_SIZE

