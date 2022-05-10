import select
import socket
import sys
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version

_LOGGER = logging.getLogger(__name__)

_REQUEST_TIMEOUT = 5
_REQUEST_RETRIES = 3
_REQUEST_RETRY_DELAY = 1

_DEFAULT_PORT = 554
_DEFAULT_TIMEOUT = 5

_DEFAULT_USERNAME = 'admin'
_DEFAULT_PASSWORD = 'admin'


class Camera(object):
    """
    A base class for a camera.

    :param str host: The hostname or IP address of the camera.
    :param int port: The port of the camera.
    :param str username: The username to use for authentication.
    :param str password: The password to use for authentication.
    :param float timeout: The number of seconds to wait for a response from the
        camera.
    """

    def __init__(self, host, port=_DEFAULT_PORT, username=_DEFAULT_USER
