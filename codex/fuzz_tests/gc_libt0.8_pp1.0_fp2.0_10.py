import gc, weakref
import socket

from ws4py.client import WebSocketBaseClient
from ws4py.exc import HandshakeError
from ws4py.exc import ExtensionParameterError
from ws4py.http import Headers
from ws4py.manager import WebSocketManager
from ws4py.websocket import WebSocket

class WebSocketClient(WebSocketBaseClient):
    """
    A websocket client.
    """
    manager = None
    """
    The manager of this websocket. It is a common
    :class:`~ws4py.manager.WebSocketManager` instance.
    """

    def handshake_headers(self):
        """
        Performs the websocket handshake.
        """
        if self.port == 80:
            location = "ws://%s%s" % (self.host, self.resource)
        elif self.is_ssl:
            location = "wss://%s:%d%s" % (self.host, self.port, self.resource)
        else:
            location = "ws://%s:%
