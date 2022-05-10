import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import protocol
from . import protocol_pb2
from . import rpc
from . import util
from . import wire
from . import wire_pb2

_logger = logging.getLogger(__name__)

_DEFAULT_TIMEOUT = 5
_DEFAULT_MAX_MESSAGE_SIZE = 64 * 1024 * 1024
_DEFAULT_MAX_MESSAGES_IN_FLIGHT = 100
_DEFAULT_MAX_MESSAGES_PER_SECOND = 100
_DEFAULT_MAX_MESSAGES_PER_SECOND_BURST = 1000
_DEFAULT_MAX_MESSAGES_PER_SECOND_BURST_DURATION = 1
_DEFAULT_MAX_MESSAGES_PER_SECOND_BURST_RESET_INTERVAL = 0.1
_DEFAULT_MAX_MESSAGES_PER_SECOND_BURST_RESET_DELAY = 0.1
_DEFAULT_MAX_MES
