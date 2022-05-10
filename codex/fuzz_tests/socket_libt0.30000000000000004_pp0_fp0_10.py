import socket
import sys
import threading
import time
import traceback
import urllib2
import urlparse

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn

from . import config
from . import log
from . import util

logger = log.get_logger()

class ProxyHandler(BaseHTTPRequestHandler):
    """
    A simple proxy handler that forwards HTTP requests to the remote server.
    """
    def __init__(self, *args, **kwargs):
        self.remote_server = kwargs.pop('remote_server')
        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)

    def do_GET(self):
        """
        Forward a GET request to the remote server.
        """
        try:
            self._do_request()
        except Exception as e:
            logger.error('Error handling request: %s' % e)
            traceback.print_exc()

    def do_POST(self):
        """
        Forward a POST request to the remote server.
