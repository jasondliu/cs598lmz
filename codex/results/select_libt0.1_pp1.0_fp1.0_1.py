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
from . import protocol
from . import util
from . import version

_logger = log.get_logger(__name__)


class Client(object):
    """
    A client for the Arvados Keep service.

    This class provides a simple interface for reading and writing
    blocks of data to the Keep service.

    :ivar str api_token: The API token to use for authentication.
    :ivar str keep_service_host: The hostname of the Keep service.
    :ivar int keep_service_port: The port of the Keep service.
    :ivar int num_retries: The number of times to retry a failed
        request.
    :ivar int timeout: The timeout in seconds for each request.
    """

    def __init__(self, api_token=None, keep_service_host=None,
                 keep_service_port=
