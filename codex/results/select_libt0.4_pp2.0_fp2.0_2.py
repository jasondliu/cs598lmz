import select
import socket
import sys
import time
import traceback

from . import __version__
from . import exceptions
from . import protocol

try:
    from . import _socks
except ImportError:
    _socks = None


class Socks5AuthError(exceptions.SocksError):
    """SOCKS5 authentication error."""


class Socks5NegotiationError(exceptions.SocksError):
    """SOCKS5 negotiation error."""


class Socks5Error(exceptions.SocksError):
    """SOCKS5 error."""


class Socks5ServerError(exceptions.SocksError):
    """SOCKS5 server error."""


class Socks5Client(object):
    """SOCKS5 client."""

    def __init__(self, proxy_addr=None, proxy_port=None, proxy_type=None,
                 rdns=True, username=None, password=None,
                 timeout=None, source_address=None,
                 socket_options=None):
        """Initialize SOCKS5 client
