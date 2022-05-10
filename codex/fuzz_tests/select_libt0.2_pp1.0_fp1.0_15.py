import select
import socket
import sys
import time
import traceback
import urllib
import urlparse

from . import __version__
from . import common
from . import compat
from . import config
from . import daemon
from . import dispatch
from . import events
from . import http
from . import http_headers
from . import http_status
from . import http_websocket
from . import log
from . import mime_types
from . import process
from . import request
from . import response
from . import server
from . import util
from . import wsgi

#------------------------------------------------------------------------------
# Constants
#------------------------------------------------------------------------------

# The default HTTP version to use in responses.
DEFAULT_HTTP_VERSION = "HTTP/1.1"

# The default maximum number of requests to handle before shutting down.
DEFAULT_MAX_REQUESTS = 100

# The default maximum number of seconds to wait for a request to complete.
DEFAULT_REQUEST_TIMEOUT = 60

# The default maximum number of seconds to wait for a connection to close.
DEFAULT_CLOSE_TIMEOUT = 5
