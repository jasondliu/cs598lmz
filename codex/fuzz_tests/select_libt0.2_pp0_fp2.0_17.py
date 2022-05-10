import select
import socket
import sys
import threading
import time
import traceback

from . import _common
from . import _constants
from . import _errors
from . import _events
from . import _util
from . import _websocket
from . import _websocket_common
from . import _websocket_extensions
from . import _websocket_server
from . import _websocket_server_extensions

__all__ = ['WebSocketServer']


class WebSocketServer(_websocket_server.WebSocketServer):
    """A WebSocket server."""

    def __init__(self, host, port, resource,
                 version=_common.DEFAULT_WEBSOCKET_VERSION,
                 origin=None, extensions=None,
                 heartbeat_freq=None, ssl_options=None,
                 http_compression=True,
                 handler_cls=_websocket_server_extensions.WebSocketRequestHandler,
                 select=select.select,
                 environ=None,
                 handler_list=None):
        """Initialize
