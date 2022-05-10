from lzma import LZMADecompressor
LZMADecompressor.decompress = LZMADecompressor.decompress

import base64
import datetime
import json
import os
import sys
import time
import zipfile

import requests

from . import __version__
from . import utils
from . import __useragent__
from . import __base_url__
from . import __default_headers__
from . import __default_params__
from . import __default_cookies__

from .exceptions import *
from .models import *

import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class Client(object):
    """
    The main client class.
    """

    def __init__(self, username=None, password=None, cookie=None, device_id=None, user_agent=None, base_url=None,
                proxies=None, verify_ssl=True):
        """
        :param username:
            The username of the account.

        :param password:
            The password of the account.

        :param cookie
