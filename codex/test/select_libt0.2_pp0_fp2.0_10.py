import select
import socket
import sys
import threading
import time
import traceback

import paramiko

from . import config
from . import log
from . import util
from . import version

# This is the maximum number of bytes to read at a time from a socket.
# It should be large enough to handle a single packet.
MAX_READ = 32768

# This is the maximum number of bytes to send at a time from a socket.
# It should be large enough to handle a single packet.
MAX_SEND = 32768

