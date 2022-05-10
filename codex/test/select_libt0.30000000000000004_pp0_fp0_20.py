import select
import socket
import sys
import threading
import time
import traceback

from . import constants
from . import errors
from . import events
from . import utils
from . import version

__all__ = [
    'Client',
    'Server',
    'ClientConnection',
    'ServerConnection',
    'ClientServerConnection',
]

log = logging.getLogger(__name__)

#: Default timeout for socket operations.
DEFAULT_TIMEOUT = 10

#: Default maximum size of a message.
DEFAULT_MAX_MESSAGE_SIZE = 1024 * 1024

#: Default maximum number of messages to receive in a single recv call.
DEFAULT_MAX_MESSAGES = 100

#: Default maximum number of messages to send in a single send call.
DEFAULT_MAX_SEND_MESSAGES = 100

#: Default maximum number of messages to receive in a single recv call.
DEFAULT_MAX_RECV_MESSAGES = 100

