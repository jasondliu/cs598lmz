import select
import signal
import socket
import sys
import time
import traceback
import urllib
import urlparse
import xml.sax.saxutils
import zlib

from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from SocketServer import ThreadingMixIn
from cStringIO import StringIO

from . import __version__
from . import compat
from . import exceptions
from . import utils
from . import wsgi
from .wsgi import get_socket
from .wsgi import get_socket_info
from .wsgi import wrap_file_in_buffer
from .wsgi import write_chunked


class ServerHandler(BaseHTTPRequestHandler):

    server_version = 'Werkzeug/' + __version__
    sys_version = ''

    def __init__(self, *args, **kwargs):
        self.chunked_read = False
        self.chunked_write = False
        self.length = 0
        self.requestline = ''
        self.request_version = ''
        self.rfile
