import select
import socket
import sys
import threading
import time
import traceback

import janus

from . import exceptions
from . import utils
from . import websocket

logger = logging.getLogger(__name__)


class Server:
    """A WebSocket server.

    This class implements a fully compliant WebSocket server as specified in
    :rfc:`6455`.  It can be used to create WebSocket servers with any
    :class:`~websockets.http.HTTPRequestHandler`; the only requirement is that
    the handler must call its :meth:`~websockets.http.HTTPRequestHandler.run_websocket`
    method to start the WebSocket handshake.

    :param host: Hostname to serve on.
    :param port: Port to serve on.
    :param ssl: SSLContext, or None.
    :param origin: Value for the ``Origin`` header.
    :param subprotocols: List of supported subprotocols in order of decreasing
        preference.
    :param extra_headers: List of additional headers to include in
