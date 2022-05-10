import select
import socket
import sys
import time
import traceback
import urllib
import urlparse

import pycurl

from . import __version__
from . import compat
from . import exceptions
from . import utils
from . import version
from . import __version__

# The default socket timeout in seconds
DEFAULT_SOCKET_TIMEOUT = 30

# The default number of retries each HTTP request should attempt
DEFAULT_RETRIES = 0

# The default backoff factor to apply between attempts after the second try
DEFAULT_BACKOFF_FACTOR = 0.1

# The default hostname to use for the User-Agent header
DEFAULT_USER_AGENT = 'python-requests/%s' % __version__

