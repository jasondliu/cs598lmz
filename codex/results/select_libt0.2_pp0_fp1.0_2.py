import select
import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import protocol
from . import utils
from . import version

# Logger is named "pika" at the root
logger = logging.getLogger(__name__)

#
# Constants
#

# The default heartbeat interval in seconds
DEFAULT_HEARTBEAT = 0

# The default connection timeout in seconds
DEFAULT_CONNECTION_TIMEOUT = 10

# The default socket timeout in seconds
DEFAULT_SOCKET_TIMEOUT = 0.25

# The default channel max
DEFAULT_CHANNEL_MAX = 0

# The default frame max
DEFAULT_FRAME_MAX = 131072

# The default locale
DEFAULT_LOCALE = 'en_US'

# The default backpressure multiplier
DEFAULT_BACKPRESSURE_MULTIPLIER = 65536

# The default max reconnection delay
DEFAULT_MAX_RECONNECTION_DELAY = 30.0

# The default
