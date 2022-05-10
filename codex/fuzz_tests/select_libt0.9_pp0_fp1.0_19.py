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

    def __init__(self, address: str, request_handler: IUnixRequestHandler):
        """
        :param address: Path to a UNIX domain socket.
        :param request_handler: A class which implements the request/response protocol.

        "request_handler" is expected to be a class with two required methods:

        def handle_request(self, request: bytes) -> Optional[bytes]:
            ...

        def disconnect(self) -> None:
            ...

        "handle_request" receives the bytes received from a
