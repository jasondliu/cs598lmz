import _struct
from _socket import error as SocketError
from _socket import *
from _socket import AF_INET6

from six import string_types
import zmq
from zmq.utils import jsonapi
import logging

from . import utils
from . import parse

from . import __version__
from .constants import URL_REGEX
from .exceptions import ConnectionClosed
from .exceptions import TimeoutExpired
from .exceptions import MessageError
from .exceptions import MessageTypeError

__all__ = ['Connection']

logger = logging.getLogger(__name__)

# TODO:
# * add shutdown and shutdown_server methods.
# * remove self.context, self.socket properties.
# * add support for ZMQ_LAST_ENDPOINT (and other socket options)

#-----------------------------------------------------------------------------
# Serialization
#-----------------------------------------------------------------------------

class CloudpickleSerializer(object):

    def __init__(self, context):
        self.context = context

