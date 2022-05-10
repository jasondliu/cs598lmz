import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse
import zlib
import zipfile

from . import _compat
from . import _util

if sys.version_info[0] == 2:
    import cookielib
    import httplib
    import urlparse
else:
    import http.cookies as cookielib
    import http.client as httplib
    import urllib.parse as urlparse


#
# Exceptions
#

class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class RedirectError(Error):
    """Raised when a request is redirected to an equal URI."""
    pass


class HTTPError(Error):
    """Raised when the HTTP error code is not 200."""
    pass


class URLError(Error):
    """Raised when a URL does not follow RFC 2396."""
    pass


class BadStatusLine(Error):
    """Raised if the status line can't be parsed
