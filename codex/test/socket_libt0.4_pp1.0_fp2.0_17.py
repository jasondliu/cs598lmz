import socket

from . import common
from . import constants
from . import exceptions
from . import utils
from . import __version__


class Client(object):
    """
    A client for the Amazon Simple Queue Service.
    """

