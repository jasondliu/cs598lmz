import codecs
codecs.register_error('ignore', codecs.ignore_errors)

# for python 2.x
try:
    from urllib.request import Request, urlopen, build_opener, install_opener
    from urllib.parse import urlencode
    from urllib.error import HTTPError
except ImportError:
    # for python 3.x
    from urllib2 import Request, urlopen, build_opener, install_opener, HTTPError
    from urllib import urlencode

import re
import time
import random

import lxml.html

from . import __version__
from . import util
from . import exception
from . import config


class Base(object):
    """
    Base class for all API classes.

    :param \*\*kwargs:
        Keyword arguments to be passed into :py:meth:`~Base.__init__`.
    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, key):
        return self.__dict
