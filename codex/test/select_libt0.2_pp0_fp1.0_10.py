import select
import socket
import sys
import time
import threading
import traceback
import Queue

from . import config
from . import log
from . import util
from . import version
from . import x509

#
# Constants
#

#
# Exceptions
#

class Error(Exception):
    """Base exception class."""

class ConnectionError(Error):
    """Connection error."""

class ProtocolError(Error):
    """Protocol error."""

class ProtocolVersionError(ProtocolError):
    """Protocol version error."""

class ProtocolTimeoutError(ProtocolError):
    """Protocol timeout error."""

class ProtocolNegotiationError(ProtocolError):
    """Protocol negotiation error."""

class ProtocolAuthenticationError(ProtocolError):
    """Protocol authentication error."""

