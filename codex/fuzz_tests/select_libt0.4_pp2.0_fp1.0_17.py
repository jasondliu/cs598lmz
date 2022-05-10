import select
import socket

from . import common
from . import errors
from . import events
from . import futures
from . import protocols
from . import transports
from . import sslproto
from .log import logger


__all__ = ['BaseEventLoop', 'SelectorEventLoop']


class _UnixSelectorEventLoop(select.epoll):
    """An epoll() based event loop using our C epoll module."""

    def __init__(self, selector=None):
        if selector is None:
            selector = select.epoll()
        super().__init__(selector)
        self._make_self_pipe()

    def _make_socket_transport(self, sock, protocol, waiter=None,
                               extra=None, server=None):
        return _UnixReadPipeTransport(self, sock, protocol, waiter,
                                      extra, server)

    def _make_ssl_transport(self, rawsock, protocol, sslcontext, waiter=None,
                            server_side=False, server_hostname=None,
                            extra=None
