import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

from netlib import http_auth

from .. import controller, version, utils
from ..protocol import http_replay, http
from ..stateobject import StateObject


class HTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """
        A special HTTP Handler which logs request and responses.
    """
    protocol_version = "HTTP/1.1"

    LOG_REQUESTS = False

    def __init__(self, connection, client_address, server, state):
        self.state = state
        self.server = server
        self.client_address = client_address
        self.connection = connection
        self.rfile = connection.makefile("rb", -1)
        self.wfile = connection.makefile("wb", 0)
        self._log()

    def _log(self):
        if self.LOG_REQUESTS:
            log.info("Request from %s:%s: %s %s %s", self.client_address[0], self.client_address[1], self.command, self.path, self
