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

