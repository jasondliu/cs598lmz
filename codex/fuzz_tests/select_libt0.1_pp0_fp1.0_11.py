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
from . import wire
from . import wire_format
from . import wire_format_pb2
from . import wire_format_pb2_grpc
from . import wire_pb2
from . import wire_pb2_grpc
from . import wire_types

_LOGGER = logging.getLogger(__name__)

_DEFAULT_MAX_MESSAGE_LENGTH = 4 * 1024 * 1024
_DEFAULT_MAX_CONCURRENT_STREAMS = 100
_DEFAULT_INITIAL_WINDOW_SIZE = 65535
_DEFAULT_MAX_FRAME_SIZE = 16384
_DEFAULT_MAX_HEADER_LIST_SIZE = 8192
_DEFAULT_GRACEFUL_SHUTDOWN_TIMEOUT = 5.0

_DEFAULT_KEEPALIVE_TIME = 2 * 60
_DEFAULT_KEEPALIVE_TIMEOUT = 20
_DEFAULT_KEEP
