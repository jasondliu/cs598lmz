import weakref
import logging

from twisted.internet.error import ConnectionAbortedError
from twisted.internet.error import ConnectionClosed
from twisted.internet.error import ConnectionDone
from twisted.internet.protocol import Protocol
from twisted.python import log

from . import _stringtransport
from . import _compat
from . import utils

logger = logging.getLogger(__name__)

_DEFAULT_SOCKET_TIMEOUT = 0.1


class WebSocket(object):
    def __init__(self, transport, on_message=None, on_data=None,
                 on_ping=None, on_pong=None, on_close=None,
                 protocols=None, extensions=None):
        """ Create new WebSocket.

        `on_message` will be called when a message has been received.

        `on_data` will be called when a data frame has been received.

        `on_ping` will be called when a ping has been received.
        `on_pong` will be called when a pong has been received.

        `on_close`
