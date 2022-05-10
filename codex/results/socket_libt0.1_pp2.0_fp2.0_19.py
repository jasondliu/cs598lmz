import socket
import sys
import threading
import time

from . import constants
from . import exceptions
from . import utils
from . import version

logger = logging.getLogger(__name__)


class Client(object):
    """
    A client for the Docker Engine API.

    Args:
        base_url (str): URL of the Docker server.
        version (str): The version of the API to use. Set to
            ``auto`` to automatically detect the server's version.
        timeout (int): Default timeout for API requests, in seconds.
        tls (bool or :py:class:`docker.tls.TLSConfig`): Enable TLS. Set to
            ``True`` to use default TLS settings. Pass an instance of
            :py:class:`docker.tls.TLSConfig` for custom TLS settings.
        user_agent (str): User agent to use for requests.
        **kwargs (dict): Arbitrary keyword arguments to set on the
            :py:class:`requests.Session` instance.

    Raises:
        docker.errors.DockerException
