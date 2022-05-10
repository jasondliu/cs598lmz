import socket
import time
import threading
import logging

from pydispatch import dispatcher

from . import const
from . import util
from . import messages as msg
from . import events as evt
from . import exceptions as ex

log = logging.getLogger(__name__)

class Client(object):
    """
    Client object for communicating with the server.
    """

    def __init__(self, host, port, timeout=5, retry=True, retry_delay=5,
                 retry_max=3, retry_backoff=2, retry_jitter=0.2,
                 retry_jitter_max=0.5, retry_jitter_factor=0.5,
                 retry_max_delay=60):
        """
        Initialize the client object.

        :param host: Hostname or IP address of the server.
        :param port: Port number of the server.
        :param timeout: Connection timeout in seconds.
        :param retry: Retry connection if it fails.
        :param retry_delay: Initial
