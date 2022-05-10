import select
import socket
import sys
import threading
import time

from . import errors
from . import util
from . import websocket


class Server(object):
    """
    A WebSocket server.

    :param host: Hostname to serve on.
    :param port: Port to serve on.
    :param ssl_only: Only allow connections over SSL (default ``False``).
    :param ssl_options: A dict of keyword arguments to pass as keyword
        arguments to the Python :mod:`ssl.wrap_socket` function.  If
        ``ssl_options`` is ``None``, then the default options will be used.
        If ``ssl_options`` is ``False``, then SSL will not be used.
        (default ``None``).
    :param heartbeat_timeout: The timeout in seconds to use for the
        heartbeat.  If ``None``, then no heartbeat will be sent.
        (default ``None``).
    :param source_address: The source address to bind to.
    :param ping_timeout: The timeout in seconds to use when waiting for a
        ping to complete
