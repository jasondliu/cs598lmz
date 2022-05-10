import select
import socket
import sys
import threading
import time
import traceback
import urllib
import urlparse

from wsgiref.handlers import format_date_time
from wsgiref.headers import Headers
from wsgiref.simple_server import WSGIRequestHandler, WSGIServer, WSGIHandler

from . import __version__
from . import config
from . import log
from . import utils
from . import wsgi


class WSGIServer(WSGIServer):
    """
    A WSGI server that handles multiple requests in parallel.
    """

    def __init__(self, *args, **kwargs):
        self.address_family = kwargs.pop('address_family', socket.AF_INET)
        self.socket_type = kwargs.pop('socket_type', socket.SOCK_STREAM)
        WSGIServer.__init__(self, *args, **kwargs)

    def get_request(self):
        while True:
            try:
                sock, address = self.socket.
