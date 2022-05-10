import select
import socket
import sys
import threading
import time

from . import common
from . import config
from . import constants
from . import errors
from . import log
from . import util
from . import version

# pylint: disable=too-many-lines

#
# Constants
#

_LOGGER = log.get_logger(__name__)

_DEFAULT_TIMEOUT = 10
_DEFAULT_RETRIES = 3

_DEFAULT_PORT = constants.DEFAULT_PORT
_DEFAULT_HOST = constants.DEFAULT_HOST

_DEFAULT_CONNECT_TIMEOUT = 10
_DEFAULT_CONNECT_RETRIES = 3

_DEFAULT_REQUEST_TIMEOUT = 10
_DEFAULT_REQUEST_RETRIES = 3

_DEFAULT_REQUEST_RETRY_DELAY = 0.1

_DEFAULT_REQUEST_RETRY_DELAY_MULTIPLIER = 1.5
_DEFAULT_REQUEST_RETRY_DELAY_MAX = 60

_
