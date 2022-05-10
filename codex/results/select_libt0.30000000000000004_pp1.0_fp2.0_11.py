import select
import socket
import sys
import threading
import time
import traceback

import six

from . import constants
from . import exceptions
from . import utils
from . import version

try:
    import ssl
except ImportError:
    ssl = None

try:
    import resource
except ImportError:
    resource = None

try:
    import fcntl
except ImportError:
    fcntl = None

_DEFAULT_TIMEOUT = object()

if sys.version_info[:2] == (2, 6):
    # Python 2.6's socket module is missing some constants.
    for _name, _value in [
        ('TCP_CORK', 3),
        ('TCP_KEEPIDLE', 4),
        ('TCP_KEEPINTVL', 5),
        ('TCP_KEEPCNT', 6),
        ('TCP_SYNCNT', 7),
        ('TCP_LINGER2', 8),
        ('TCP_DEFER_ACCEPT', 9),
        ('TCP_
