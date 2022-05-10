import select
import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version

_logger = logging.getLogger(__name__)

_DEFAULT_TIMEOUT = constants.DEFAULT_TIMEOUT
_DEFAULT_RETRIES = constants.DEFAULT_RETRIES
_DEFAULT_BACKOFF = constants.DEFAULT_BACKOFF
_DEFAULT_BACKOFF_CAP = constants.DEFAULT_BACKOFF_CAP
_DEFAULT_CHUNK_SIZE = constants.DEFAULT_CHUNK_SIZE
_DEFAULT_USER_AGENT = constants.DEFAULT_USER_AGENT
_DEFAULT_MAX_REDIRECTS = constants.DEFAULT_MAX_REDIRECTS
_DEFAULT_PROXY_HOST = constants.DEFAULT_PROXY_HOST
_DEFAULT_PROXY_PORT = constants.DEFAULT_PROXY_PORT
_DEFAULT_PROXY_USER = constants.DEFAULT_PROXY_USER
_DEFAULT_PROXY_PASS = constants
