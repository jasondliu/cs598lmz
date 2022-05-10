import select
import sys
import time
import traceback
import urllib
import urlparse

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from threading import Thread

from . import common
from . import config
from . import constants
from . import errors
from . import log
from . import util

# The following are used to parse the request URL.
_SCHEME, _NETLOC, _PATH, _PARAMS, _QUERY, _FRAGMENT = range(6)

# The following are used to parse the request query.
_QUERY_KEY, _QUERY_VALUE = range(2)

# The following are used to parse the request headers.
_HEADER_KEY, _HEADER_VALUE = range(2)

# The following are used to parse the request body.
_BODY_KEY, _BODY_VALUE = range(2)

# The following is used to parse the request body when it is a form.
