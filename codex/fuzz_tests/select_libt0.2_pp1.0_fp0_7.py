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
    A client for the Docker Engine API.

    Args:
        base_url (str): URL of the Docker server.
        version (str): The version of the API to use. Set to ``auto`` to
            automatically detect the server's version. Default: ``auto``.
        timeout (int): Default timeout for API calls, in seconds.
            Default: ``None``.
        tls (bool or docker.tls.TLSConfig): Enable TLS. Default: ``False``.
        user_agent (str): User agent to use for requests.
            Default: ``docker-sdk-python``.
        **kwargs (dict): Arbitrary keyword arguments.
    """
    def __init__(self, base_url=
