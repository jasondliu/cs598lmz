import select
import socket
import sys
import time
import threading
import traceback
import urllib
import urllib2
import urlparse

from . import common
from . import config
from . import control
from . import daemon
from . import dns
from . import event
from . import log
from . import network
from . import util

# The maximum number of bytes to read from a socket at a time.
SOCKET_READ_SIZE = 65536

# The maximum number of bytes to send to a socket at a time.
SOCKET_WRITE_SIZE = 65536

# The maximum number of bytes to read from a socket at a time when we're
# receiving an HTTP request.
HTTP_REQUEST_READ_SIZE = 65536

# The maximum number of bytes to read from a socket at a time when we're
# receiving an HTTP response.
HTTP_RESPONSE_READ_SIZE = 65536
