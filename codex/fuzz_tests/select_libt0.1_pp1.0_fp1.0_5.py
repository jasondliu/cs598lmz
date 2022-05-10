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
from wsgiref.simple_server import WSGIRequestHandler, WSGIServer
from wsgiref.util import request_uri

from . import __version__
from . import wsgi
from . import wsgi_file_wrapper
from . import wsgi_line_reader
from . import wsgi_line_writer
from . import wsgi_server
from . import wsgi_utils
from . import wsgi_websocket

# ------------------------------------------------------------------------------
# wsgi_server_base
# ------------------------------------------------------------------------------

class wsgi_server_base(object):

    def __init__(self, host, port, application,
                 server_name=None,
                 server_version=None,
                 server_software=None,
                 server_host=None,
                 server_port=None,
                 server_protocol=
