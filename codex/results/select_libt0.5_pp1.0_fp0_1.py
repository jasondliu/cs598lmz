import select
import socket
import sys
import traceback
import urllib.parse
import logging

from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime

from . import utils
from . import http_codes
from . import http_methods
from . import http_parser
from . import http_response
from . import http_request
from . import http_header
from . import http_server
from . import http_error


logger = logging.getLogger(__name__)


class HttpServer(http_server.HttpServer):

    def __init__(self, host, port):
        super().__init__(host, port)
        self.__connections = {}
        self.__sockets = []

    def run(self):
        try:
            self.__sockets.append(self._socket)
            while True:
                readable, writable, exceptional = select.select(
                    self.__sockets, [], self.__sockets)
                for s in readable:
                    if s
