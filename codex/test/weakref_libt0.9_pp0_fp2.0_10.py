import weakref
import itertools
import sys
import collections

from molotov.tcp import (TCPConnection, TCPServer, TCPAcceptor,
                         TCPClient)


class Mocket(object):
    """
    A socket on which we can record and replay.

    See :ref:`socket-mocks` to learn more.
    """

    socket = socket.socket
    HOST = '127.0.0.1'
    PORT = 3333
    AF_INET = getattr(socket, 'AF_INET', None)
    SOCK_STREAM = getattr(socket, 'SOCK_STREAM', None)
    SOCK_DGRAM = getattr(socket, 'SOCK_DGRAM', None)
    MAX_EVENT_NUMBER = 1000

