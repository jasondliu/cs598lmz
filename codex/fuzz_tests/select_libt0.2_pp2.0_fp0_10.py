import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import exceptions
from . import log
from . import util
from . import version

# Logger is here for backwards compatibility
logger = log.get_logger(__name__)


class Client(object):
    """
    A client for the Docker Engine API.

    Args:
        base_url (str): URL of the Docker server.
        version (str): The version of the API to use. Set to ``auto`` to
            automatically detect the server's version. Default: ``1.24``
        timeout (int): Default timeout for API calls, in seconds.
            Default: ``60``
        tls (bool or :py:class:`docker.tls.TLSConfig`): Enable TLS. Default:
            ``False``
        user_agent (str): User agent to use for requests. Default:
            ``docker-sdk-python/{docker-py-version}``
        credstore_env (dict): Environment variables to
