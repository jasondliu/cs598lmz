import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import version
from . import xlog
from . import xlogviewer
from . import xlogserver
from . import xlogviewer_pb2

_logger = log.get_logger(__name__)

_DEFAULT_PORT = config.get_config().getint('xlogviewer', 'port')

_MAX_CONNECTIONS = config.get_config().getint('xlogviewer', 'max_connections')

_MAX_REQUEST_SIZE = config.get_config().getint('xlogviewer', 'max_request_size')

_MAX_RESPONSE_SIZE = config.get_config().getint('xlogviewer', 'max_response_size')

_MAX_REQUEST_TIME = config.get_config().getint('xlogviewer', 'max_request_time')

_MAX_REQUEST_TIME_IDLE = config.get_config().
