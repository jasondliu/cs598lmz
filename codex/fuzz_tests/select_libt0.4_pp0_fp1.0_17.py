import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import constants
from . import errors
from . import events
from . import futures
from . import protocol
from . import transports
from .log import logger

__all__ = ['Server']


class Server:

    def __init__(self, *, loop=None):
        if loop is None:
            loop = asyncio.get_event_loop()
        self._loop = loop
        self._waiters = []
        self._sockets = []
        self._serving = False
        self._handler = None
        self._server_task = None
        self._closing = False
        self._closed = False
        self._connections = {}
        self._connections_lock = threading.Lock()
        self._protocol_factory = protocol.ServerFactory()
        self._protocol_factory.set_server(self)

    def close(self):
        if self._closed:
            return
        self._closing = True
        for sock in self._s
