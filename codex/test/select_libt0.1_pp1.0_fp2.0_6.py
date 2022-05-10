import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import errors
from . import log
from . import messages
from . import utils
from . import version

# pylint: disable=too-many-lines

_LOGGER = log.get_logger(__name__)

_DEFAULT_TIMEOUT = 10

_DEFAULT_CONNECT_TIMEOUT = 5

_DEFAULT_RECONNECT_TIMEOUT = 5

_DEFAULT_RECONNECT_MAX_ATTEMPTS = 3

_DEFAULT_RECONNECT_BACKOFF_FACTOR = 1.5
