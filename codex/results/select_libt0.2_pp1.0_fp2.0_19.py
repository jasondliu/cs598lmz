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
from . import util

# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-locals
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
# pylint: disable=too-many-nested-blocks
# pylint: disable=too-many-arguments
# pylint: disable=too-many-lines

_logger = log.get_logger(__name__)


class Client(object):
    """
    The Client class is used to communicate with a server.

    It is responsible for sending and receiving messages.
    """

    def __init__(self,
                 host,
                 port,
                 config_dir,
                 data_dir,

