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

_DEFAULT_RETRY_DELAY = 5

_DEFAULT_RETRY_COUNT = 3

_DEFAULT_RETRY_BACKOFF = 2

_DEFAULT_RETRY_JITTER = 0.1

_DEFAULT_RETRY_MAX_DELAY = 60

_DEFAULT_RETRY_MAX_JITTER = 0.5

_DEFAULT_RETRY_MAX_TIMEOUT = 60

_DEFAULT_RETRY_MAX_RETRIES = 10

_DEFAULT_RETRY_MAX_BACKOFF = 10

_DEFAULT_RETRY_MAX_DELAY_JITTER =
