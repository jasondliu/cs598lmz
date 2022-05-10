import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import constants
from . import errors
from . import log
from . import util
from . import version
from . import xlog
from . import xlogviewer
from .xlog import XLog, XLogReader

# The following are used to communicate with the server.
#
# The client sends a request to the server, which is a 4-byte integer
# indicating the request type, followed by the request-specific data.
#
# The server responds with a 4-byte integer indicating the response type,
# followed by the response-specific data.
#
# If the server cannot complete the request, it sends a 4-byte integer
# indicating the error type, followed by the error-specific data.
#
# The server may also send unsolicited messages to the client.  These
# messages have a 4-byte integer indicating the message type, followed by
# the message-specific data.
#
# The server may also send an error to the client.  These errors have a
# 4-byte integer indicating the error
