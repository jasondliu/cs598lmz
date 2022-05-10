import select
import socket
import sys
import threading
import time
import traceback
import urllib.parse
import urllib.request

from OpenSSL import crypto, SSL
from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.ssl import ClientContextFactory
from twisted.protocols.basic import LineReceiver

from . import __version__
from . import config
from . import log
from . import util
from . import version

#: The default port for HTTP connections.
DEFAULT_HTTP_PORT = 80

#: The default port for HTTPS connections.
DEFAULT_HTTPS_PORT = 443

#: The maximum size of the buffer used to read HTTP responses.
MAX_BUFFER_SIZE = 1024 * 1024

#: The maximum number of bytes to read when checking for a header.
MAX_HEADER_CHECK = 1024

#: The maximum number of bytes to read when checking for a header.
MAX_HEADER_SIZE = 1024 * 1024

#: The maximum number of bytes to
