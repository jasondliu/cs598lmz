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
from . import protocol
from . import util
from . import version

# pylint: disable=too-many-lines

_LOGGER = log.get_logger(__name__)

_DEFAULT_TIMEOUT = 10

_DEFAULT_RECONNECT_WAIT = 5

_DEFAULT_RECONNECT_MAX_ATTEMPTS = 10

_DEFAULT_RECONNECT_BACKOFF_FACTOR = 1.5

_DEFAULT_RECONNECT_JITTER_FACTOR = 0.5

_DEFAULT_RECONNECT_JITTER_MAX = 5

_DEFAULT_RECONNECT_JITTER_MIN = 1

_DEFAULT_RECONNECT_JITTER_SEED = 0

_DEFAULT_RECONNECT_JITTER_ENABLED = True

_DEFAULT_RECON
