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

_DEFAULT_RETRY_DELAY_MAX = 60

_DEFAULT_RETRY_DELAY_MULTIPLIER = 1.5

_DEFAULT_RETRY_DELAY_JITTER = 0.1

_DEFAULT_RETRY_DELAY_JITTER_MAX = 0.5

_DEFAULT_RETRY_DELAY_JITTER_MULTIPLIER = 1.5

_DEFAULT_RETRY_DELAY_JITTER_MAX_MULTIPLIER = 1.5

_DEFAULT_RE
