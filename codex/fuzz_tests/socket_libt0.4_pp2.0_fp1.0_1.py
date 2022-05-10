import socket
import sys
import time

from . import _constants
from . import _errors
from . import _util
from . import _util_socket
from . import _util_ssl
from . import _util_wsgi
from . import _wsgi_wrapper
from . import _wsgi_server


__all__ = [
    'WSGIServer',
    'WSGIServerConnection',
    'WSGIServerHandler',
    'WSGIServerRequest',
    'WSGIServerResponse',
]


class WSGIServer(_wsgi_server.WSGIServer):
    """
    A WSGI server that can be used to serve a WSGI application.

    This is a wrapper around the `wsgiref.simple_server.WSGIServer`
    class that adds support for SSL and IPv6.

    The constructor takes the same arguments as the
    `wsgiref.simple_server.WSGIServer` constructor, except for the
    `server_address` argument.

    The `server_address` argument can be a tuple of the form
    `
