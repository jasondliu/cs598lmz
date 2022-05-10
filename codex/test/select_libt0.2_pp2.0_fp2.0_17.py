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

#
# This module implements a simple TCP/IP server.  It is intended to be used
# for testing the client.  It is not intended to be used for production
# purposes.
#

#
# The server is implemented as a singleton.  The server is started by calling
# the start() method.  The server is stopped by calling the stop() method.
#
# The server listens on a specified port.  When a client connects, the server
# spawns a new thread to handle the connection.  The server supports multiple
# concurrent connections.
#
# The server supports the following commands:
#
#   * echo
#   * sleep
#   * shutdown
#
# The echo command simply echoes the specified text back to the client.
#
# The sleep command sleeps for the specified number of seconds.
#
# The shutdown command shuts down the server.
#
# The server also supports the following commands:
#
#   * get
