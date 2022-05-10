import select
import socket
import sys
import time
import threading
import traceback

from . import common
from . import config
from . import constants
from . import log
from . import util

# This is the maximum number of bytes that can be sent in a single message.
# This is a limit imposed by the protocol.
MAX_MESSAGE_SIZE = 1000000

# This is the maximum number of bytes that can be received in a single message.
# This is a limit imposed by the protocol.
MAX_RECEIVE_SIZE = 1000000

# This is the maximum number of bytes that can be sent in a single message.
# This is a limit imposed by the protocol.
MAX_SEND_SIZE = 1000000

# This is the maximum number of bytes that can be sent in a single message.
# This is a limit imposed by the protocol.
MAX_SEND_SIZE = 1000000

# This is the maximum number of bytes that can be sent in a single message.
# This is a limit imposed by the protocol.
MAX_SEND_SIZE = 1000000

# This is the maximum number of
