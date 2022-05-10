import select
import socket
import sys
import time
import traceback

from . import exceptions
from . import utils
from . import version
from . import websocket
from . import websocket_server

try:
    from . import ssl_compat
except ImportError:
    ssl_compat = None

try:
    import ssl
except ImportError:
    ssl = None

try:
    import thread
except ImportError:
    thread = None

try:
    import threading
except ImportError:
    threading = None

try:
    import Queue
except ImportError:
    Queue = None


__version__ = version.__version__
__license__ = version.__license__
__author__ = version.__author__


class WebSocketWSGI(object):
    """
    WebSocket WSGI application.
    """

    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        websocket =
