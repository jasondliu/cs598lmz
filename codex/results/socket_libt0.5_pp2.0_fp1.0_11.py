import socket
import struct
import threading
import time
import traceback

from . import constants
from . import util
from . import wsproto
from .errors import InvalidStateError
from .errors import WebSocketProtocolError
from .logging import get_logger
from .streams import StreamReader, StreamWriter
from .websocket import WebSocketCommonProtocol

__all__ = ['WebSocketServerProtocol']


class WebSocketServerProtocol(WebSocketCommonProtocol):
    """A WebSocket server protocol.

    This implements :class:`~websockets.server.WebSocketServerProtocol`
    for use with :func:`~websockets.server.serve`.

    """
    is_client = False
    side = 'server'

    def __init__(
            self, *,
            host=None, port=None, secure=False,
            timeout=10, max_size=2 ** 20, max_queue=2 ** 5, read_limit=2 ** 16,
            write_limit=2 ** 16, ping_interval=20, close_timeout
