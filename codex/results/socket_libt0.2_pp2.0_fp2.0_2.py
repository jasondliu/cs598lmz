import socket
import sys
import threading
import time
import traceback
import urllib
import urllib2
import urlparse

from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from SocketServer import ThreadingMixIn

from . import __version__
from . import config
from . import utils

logger = logging.getLogger(__name__)

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><head><title>%s</title></head>' % config.NAME)
            self.wfile.write('<body><p>%s</p>' % config.NAME)
            self.wfile.write('<p>Version %s</p>' % __version__)
            self.w
