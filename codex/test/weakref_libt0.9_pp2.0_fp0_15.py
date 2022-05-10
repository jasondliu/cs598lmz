import weakref
import logging

from twisted.internet.error import ConnectionAbortedError
from twisted.internet.error import ConnectionClosed
from twisted.internet.error import ConnectionDone
from twisted.internet.protocol import Protocol
from twisted.python import log

from . import _stringtransport
from . import _compat
from . import utils

logger = logging.getLogger(__name__)

_DEFAULT_SOCKET_TIMEOUT = 0.1


