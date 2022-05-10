import mmap
import re
import sys
import time

from . import exceptions
from . import util
from . import constants as const
from . import __version__

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse


class Client(object):
    """
    Client class for interacting with the API.

    :param str username: Username to authenticate with
    :param str password: Password to authenticate with
    :param str api_url: URL to the API endpoint
    :param str api_key: API key to use
    :param bool verify: Whether to verify SSL certs
    :param str user_agent: User agent to use
    :param int timeout: Timeout for requests
    :param bool debug: Whether to enable debug logging
    """

    def __init__(self, username=None, password=None, api_url=None, api_key=None,
                 verify=True, user_
