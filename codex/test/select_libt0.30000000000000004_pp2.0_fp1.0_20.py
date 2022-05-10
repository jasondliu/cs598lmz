import select
import socket
import sys
import time
import traceback
import urllib
import urlparse

import pycurl

from . import __version__
from . import log
from . import utils
from . import config
from . import exceptions

class CurlError(exceptions.Error):
    pass

class Curl(object):
    """
    A wrapper around pycurl that provides a higher-level interface.

    This class is not thread-safe.
    """
