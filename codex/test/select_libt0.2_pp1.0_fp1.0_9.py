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
from . import errors
from . import file_transfer
from . import log
from . import utils
from . import version_utils
from . import xattr

# The default number of seconds to wait for a response from the server.
DEFAULT_TIMEOUT = 300

# The default number of seconds to wait for a response from the server
# when performing a HEAD request.
DEFAULT_HEAD_REQUEST_TIMEOUT = 30

# The default number of seconds to wait for a response from the server
# when performing a GET request.
DEFAULT_GET_REQUEST_TIMEOUT = 300

# The default number of seconds to wait for a response from the server
# when performing a PUT request.
DEFAULT_PUT_REQUEST_TIMEOUT = 300

