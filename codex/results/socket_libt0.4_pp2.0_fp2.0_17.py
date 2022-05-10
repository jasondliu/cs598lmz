import socket
import sys
import time

from . import config
from . import exceptions
from . import log
from . import util
from . import version

_log = log.get_logger(__name__)


class Client(object):
    """
    The Client object is used to interact with the API.

    :param str api_key: The API key to use with the client.
    :param str api_version: The API version to use with the client.
    :param str api_url: The API URL to use with the client.
    :param str user_agent: The User-Agent string to use with the client.
    :param int timeout: The timeout (in seconds) to use with the client.
    :param bool verify_ssl: Whether to verify SSL or not.
    :param str ca_bundle: The CA bundle to use for verifying SSL.
    :param str proxy: The proxy to use for the client.
    :param bool debug: Whether to enable debug mode or not.
    """

    def __init__(self,
                 api_key=None,
                 api_version=
