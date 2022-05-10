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

# pylint: disable=too-many-lines

# pylint: disable=too-many-instance-attributes
class Client(object):
    """
    A client for the DVID server.

    Attributes:
        server:
            The server address.
        port:
            The server port.
        uuid:
            The UUID of the data instance.
        data_name:
            The name of the data instance.
        data_type:
            The type of the data instance.
        versioned:
            Whether the data instance is versioned.
        readonly:
            Whether the data instance is read-only.
        http_timeout:
            The timeout for HTTP requests.
        http_retries:
            The number of times to retry HTTP requests.
        http_retry_interval:
            The
