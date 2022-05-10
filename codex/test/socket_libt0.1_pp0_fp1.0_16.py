import socket
import sys
import threading
import time
import traceback
import urllib
import urlparse

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn

from . import config
from . import log
from . import util
from . import version

# -----------------------------------------------------------------------------
# --SECTION--                                                 class HttpServer
# -----------------------------------------------------------------------------

class HttpServer (ThreadingMixIn, HTTPServer):
  """HTTP server with threading support"""

  def __init__ (self, server_address, handler):
    HTTPServer.__init__(self, server_address, handler)
    self.daemon_threads = True
    self.allow_reuse_address = True

# -----------------------------------------------------------------------------
# --SECTION--                                                 class HttpHandler
# -----------------------------------------------------------------------------

class HttpHandler (BaseHTTPRequestHandler):
  """HTTP request handler"""

  def __init__ (self, request, client_address, server):
    self.__server = server
