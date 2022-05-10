import mmap
import os
import re
import sys
import time
import urllib
import urllib2
import urlparse
import zlib

import pycurl

from . import config
from . import utils

# ------------------------------------------------------------------------------
#
class Downloader(object):
    """
    Downloader class.
    """

    # --------------------------------------------------------------------------
    #
    def __init__(self, logger=None, session=None):
        """
        Initialize the downloader.
        """

        self._logger = logger or utils.get_null_logger()
        self._session = session

        self._curl = pycurl.Curl()
        self._curl.setopt(pycurl.NOSIGNAL, 1)
        self._curl.setopt(pycurl.FOLLOWLOCATION, 1)
        self._curl.setopt(pycurl.MAXREDIRS, 5)
        self._curl.setopt(pycurl.CONNECTTIMEOUT, 30)
        self._curl.setopt(pycurl.TIMEOUT,
