import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import control
from . import crypto
from . import log
from . import messages
from . import network_util
from . import peer
from . import protocol
from . import relay
from . import statistics
from . import util

# The maximum number of bytes that can be sent in a single UDP packet.
MAX_UDP_PACKET_SIZE = 65536

# The maximum number of bytes that can be sent in a single TCP packet.
MAX_TCP_PACKET_SIZE = 65536

# The maximum number of bytes that can be sent in a single TCP packet.
MAX_TCP_RECEIVE_SIZE = 65536

# The maximum number of bytes that can be sent in a single UDP packet.
MAX_UDP_RECEIVE_SIZE = 65536

# The maximum number of bytes that can be sent in a single UDP packet.
MAX_UDP_RECEIVE_SIZE = 65536

# The maximum number of bytes that can
