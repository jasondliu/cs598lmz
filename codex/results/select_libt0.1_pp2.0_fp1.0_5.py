import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import errors
from . import log
from . import messages
from . import utils
from . import version

_logger = log.get_logger(__name__)


class Client(object):
    """
    Client for the server.
    """

    def __init__(self, host, port, timeout=None,
                 username=None, password=None,
                 key=None, cert=None, ca_certs=None,
                 ssl_version=None, ssl_ciphers=None,
                 ssl_options=None, ssl_context=None,
                 ssl_server_hostname=None,
                 ssl_match_hostname=True,
                 ssl_check_hostname=True,
                 ssl_assert_fingerprint=None,
                 ssl_assert_fingerprint_sha256=None,
                 ssl_assert_hostname=None,
                 ssl_assert
