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
from . import _websocket_server

__all__ = ['WebSocketServer']


class WebSocketServer(_websocket_server.WebSocketServer):
    """A websocket server implementation.

    This class implements a fully compliant WebSocket server as defined
    in `RFC 6455`_.  It can be used to create a standalone WebSocket
    server, or be combined with other web frameworks and server
    implementations.

    The server can optionally be run in threading mode, which is enabled
    by default.  In threading mode, the server will start a new thread
    to handle each incoming connection in parallel.  Alternatively, the
    server can be run in non-threading mode, which allows the server to
    be integrated with other event loops.  In non-threading mode, the
    server will call the `handle_request` method for each incoming
   
