import select
import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version

__all__ = ['Client']

logger = logging.getLogger(__name__)


class Client(object):
    """
    A client for the Docker Engine API.

    Args:
        base_url (str): URL to the Docker server. Defaults to the
            value of the DOCKER_HOST environment variable.
        version (str): The version of the API to use. Set to ``auto``
            to automatically detect the server's version. Defaults to
            ``1.21``.
        timeout (int): Default timeout for API requests, in seconds.
            Defaults to ``None`` (no timeout).
        tls (bool or :py:class:`docker.tls.TLSConfig`): Enable TLS.
            Set to ``True`` to use the host's certificates or pass a
            :py:class:`docker.tls.TLSConfig` object for custom
            configuration. Defaults
