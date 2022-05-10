import select
import socket
import sys
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
    The Client class is the main interface to the server.

    It handles the connection to the server, and provides methods to
    send and receive messages.

    The Client class is a context manager, so it can be used with the
    ``with`` statement.

    Example::

        with Client(...) as client:
            client.send(...)
            client.receive()

    """
