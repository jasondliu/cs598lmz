import ctypes
import ctypes.util
import threading
import sqlite3

from errno import *
from urllib import unquote_plus, quote
from posixpath import normpath

try:
    from httplib import responses
except ImportError:
    from http.client import responses

__author__ = "Andrew Cutler <andrew@panoptic.com>"
__version__ = "0.14"

# http://tools.ietf.org/html/rfc4918#section-9.7
#
# The PRECONDITION_FAILED status code (412) indicates that one or more conditions
# given in the request header fields evaluated to false when tested on the server.
# This response code allows the client to place preconditions on the current resource
# metainformation (header field data) and thus prevent the requested method from being
# applied to a resource other than the one intended.

PRECONDITION_FAILED = 412

# http://tools.ietf.org/html/rfc4918#section-11.2
#
# A single resource MAY be identified by many different URIs.
# For example, an article might have a
