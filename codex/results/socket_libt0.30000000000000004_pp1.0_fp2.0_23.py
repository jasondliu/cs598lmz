import socket
import sys
import threading
import time

from . import config
from . import constants
from . import exceptions
from . import utils
from . import version
from .log import logger


class Client(object):
    """
    A client for the Docker Engine API.

    Args:
        base_url (str): URL of the Docker server.
        version (str): The version of the API to use. Set to
            ``auto`` to automatically detect the server's version.
        timeout (int):
            The timeout in seconds to use for requests to the server.
            If not set, a default value is used.
        tls (bool or TLSConfig):
            Enable TLS. If set to ``True``, use the host's
            certificate. If set to a :py:class:`TLSConfig` object,
            use it to set up the client's TLS configuration.
        user_agent (str):
            The user agent to use for requests.
        version_check (bool):
            Check for the latest version of docker-py on startup.
            Default: ``True``
        **kwargs:
