import select
import socket
import ssl
import sys
import threading
import time
import traceback

from concurrent import futures

from . import compat
from . import config
from . import crypto
from . import events
from . import exceptions
from . import http
from . import log
from . import protocol
from . import util
from . import websocket

__all__ = ["Client", "connect"]

logger = log.get_logger(__name__)


class Client:
    """
    A Client is a WebSocket connection to a URL.
    """
    def __init__(self, url, timeout=10, subprotocols=None, ssl_context=None,
                 headers=None, ping_interval=0, ping_timeout=None, **kwds):
        """
        Create a new WebSocket connection to *url*.

        *url* is a string like "ws://example.com/chat".

        *timeout* is the maximum time in seconds to wait for the server
        response. The default is 10.

        *subprotocols* is an optional list of strings
