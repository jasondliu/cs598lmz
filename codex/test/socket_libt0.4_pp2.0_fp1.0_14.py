import socket
import sys
import time
import urllib
import urlparse

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from threading import Thread

from . import config
from . import constants
from . import utils
from . import xbmc_helper
from .logger import log
from .playback import Playback

class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """Respond to a GET request."""
        log.debug("Request: %s" % self.path)

        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.index_html())

        elif self.path == '/playback':
            self.send_
