import socket
import sys
import threading
import time
import traceback

from datetime import datetime

import requests
from requests.exceptions import ConnectionError

from . import exceptions
from . import utils
from .state import State
from .utils import get_logger
from .utils import get_platform
from .utils import get_version
from .utils import is_valid_daemon_address
from .utils import split_address

logger = get_logger(__name__)

DEFAULT_TIMEOUT = 5

# The daemon connection is created as a singleton to ensure that
# we only have one connection to a daemon at a time.
class DaemonConnection(object):
    """DaemonConnection class to communicate with a daemon."""
    def __init__(self, url, timeout=DEFAULT_TIMEOUT, ssl_verify=True):
        self._url = url
        self._timeout = timeout
        self._ssl_verify = ssl_verify

        self._session = requests.Session()
        self._session.mount('http://', requests.adapters.HTTP
