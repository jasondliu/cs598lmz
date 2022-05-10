import select
import socket
import sys
import threading
import time
import traceback
import urllib
import urlparse
import xml.dom.minidom

from . import config
from . import log
from . import util
from . import xmpp

#
# Constants
#

# The maximum number of bytes to read from a socket at a time.
MAX_READ = 1024

# The maximum number of bytes to write to a socket at a time.
MAX_WRITE = 1024

# The maximum number of bytes to read from a socket before closing it.
MAX_TOTAL_READ = 1024 * 1024

# The maximum number of bytes to write to a socket before closing it.
MAX_TOTAL_WRITE = 1024 * 1024

# The maximum number of bytes to buffer before flushing.
MAX_BUFFER = 1024 * 1024

# The maximum number of bytes to buffer before closing the socket.
MAX_BUFFER_TOTAL = 1024 * 1024 * 10

# The maximum number of bytes to buffer before flushing.
MAX_BUFFER_SIZE = 1024 * 1024

