import selectors
import socket
import sys
from contextlib import closing
from typing import NoReturn, Optional

from unix_sockets import UnixStreamServer
from unix_sockets.constants import SOCKET_BACKLOG, SOCKET_BUFFER_SIZE
from unix_sockets.exceptions import SocketServerError
from unix_sockets.interfaces import IUnixRequestHandler


class UnixSocketServer:
    """
    A base class for Unix domain socket servers.

    Carries the responsibility for binding the server to a listening address and
    handling client connections.
    """

