import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version
from . import __version__

logger = logging.getLogger(__name__)


class Client(object):
    """
    A client for the Pusher HTTP API.

    :param app_id: The Pusher app ID.
    :param key: The Pusher app key.
    :param secret: The Pusher app secret.
    :param ssl: Whether to use SSL.
    :param host: The host to connect to.
    :param port: The port to connect to.
    :param timeout: The timeout in seconds.
    :param cluster: The Pusher app cluster.
    :param backend: The backend to use.
    :param json_encoder: The JSON encoder to use.
    :param json_decoder: The JSON decoder to use.
    :param ssl_cert_path: The path to the SSL certificate.
    :param ssl_cert_reqs: Whether a certificate is required from
