import socket
import sys
import threading
import time

from . import _base
from . import _util
from . import _win_inet_pton
from ._util import _ip_address_types


def _resolve_addr(host, port):
    if isinstance(host, _ip_address_types):
        return host, port
    return socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM)[0][4]


class _TCPClient(_base.BaseClient):
    def __init__(self, host, port, timeout, source_address, socket_options):
        self._host, self._port = _resolve_addr(host, port)
        self._timeout = timeout
        self._source_address = source_address
        self._socket_options = socket_options
        self._sock = None

    def _create_socket(self, family):
        sock = socket.socket(family, socket.SOCK_STREAM)
        if self._timeout is not None:
            sock.settimeout(self._timeout)

