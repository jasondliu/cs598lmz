import socket
import sys
import time

from . import constants
from . import exceptions
from . import utils
from . import version

log = logging.getLogger(__name__)


class Client(object):
    """
    A client for the Docker Engine API.

    Args:
        base_url (str): URL to the Docker server.
        version (str): The version of the API to use. Set to
            ``auto`` to automatically detect the server's version.
        timeout (int): Default timeout, in seconds, for API requests.
        tls (bool or :py:class:`docker.tls.TLSConfig`): Enable TLS. If set to
            ``True``, ``client_cert`` and ``client_key`` must also be provided.
            If set to ``False``, TLS is disabled. If set to a
            :py:class:`docker.tls.TLSConfig` object, TLS is enabled, and the
            specified options are applied.
        client_cert (str): Path to the client's TLS certificate file.
        client_key (str): Path to the client
