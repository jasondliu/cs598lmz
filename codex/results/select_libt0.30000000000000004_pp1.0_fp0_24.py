import select
import socket
import sys
import time
import traceback

from . import constants
from . import exceptions
from . import util
from . import version
from . import websocket
from . import xormasker
from .logger import create_logger
from .py3compat import b, bytes_type, bytearray_type, dict_keys, dict_values, \
    integer_types, iteritems, string_types, text_type, PY3, xrange

if PY3:
    from urllib.parse import urlparse
else:
    from urlparse import urlparse

__all__ = ['WebSocket']

logger = create_logger(__name__)


class WebSocket(object):
    """
    Low level WebSocket interface.

    This class is based upon :class:`threading.Thread` and provides
    low level interface for WebSocket.  It's mainly for WebSocket
    servers.  For high level interface, see :class:`websocket.WebSocketApp`.

    This class provides following events:

    - ``on_open
