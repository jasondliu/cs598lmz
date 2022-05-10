import select
import socket
import sys
import time
import traceback
import xml.sax
import xml.sax.handler
import xml.sax.xmlreader

from xml.sax.saxutils import XMLGenerator

from . import constants
from . import saxutils
from . import transport
from . import utils

#
# exceptions
#

class Error(Exception):
    """Base class for exceptions in this module."""

class TransportError(Error):
    """HTTP transport error.

    This exception is raised by the HTTP transport layer (L{HTTPConnection}
    or L{HTTPSTransport}) when an error occurs.  It may be raised
    synchronously or asynchronously.
    """

    def __init__(self, host, errcode, errmsg, headers, ose):
        Error.__init__(self)
        self.host = host
        self.errcode = errcode
        self.errmsg = errmsg
        self.headers = headers
