import socket
import sys
import time

from . import config
from . import constants
from . import exceptions
from . import utils
from . import version

__all__ = ['Client']


class Client(object):
    """A client for the Pusher HTTP API.

    :param app_id: The id of your Pusher app.
    :param key: The key for your Pusher app.
    :param secret: The secret for your Pusher app.
    :param ssl: Whether to use SSL for requests.
    :param host: The host to use for requests.
    :param port: The port to use for requests.
    :param timeout: The timeout for HTTP requests.
    :param cluster: The cluster to use for requests.
    :param backend: The backend to use for requests.
    :param ssl_certfile: The SSL certfile to use for requests.
    :param ssl_keyfile: The SSL keyfile to use for requests.
    """

    def __init__(self, app_id, key, secret, ssl=True, host=None, port=None,

