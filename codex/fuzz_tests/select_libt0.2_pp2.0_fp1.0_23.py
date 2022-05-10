import select
import sys
import time
import traceback

from . import _util
from . import _winapi
from . import constants
from . import events
from . import futures
from . import locks
from . import protocols
from . import tasks
from . import transports
from .log import logger


__all__ = ('BaseEventLoop', 'SelectorEventLoop', 'ProactorEventLoop',
           'NewSelectorEventLoop', 'NewProactorEventLoop', 'DefaultEventLoopPolicy')


class _UnixSelectorEventLoop(selectors.BaseSelector):
    """Selector event loop for UNIX systems."""

    def __init__(self, selector):
        super().__init__(selector)
        self._make_self_pipe()

    def _make_socket_transport(self, sock, protocol, waiter=None,
                               extra=None, server=None):
        return _UnixSelectorSocketTransport(self, sock, protocol, waiter,
                                            extra, server)

    def _make_ssl_transport(self, rawsock, protocol, sslcontext, waiter
