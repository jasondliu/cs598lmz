import mmap
# Test mmap.mmap change
# pylint: disable=W0622

from gevent.fileobject import FileObject
from gevent.server import StreamServer
import gevent
from collections import deque

# pylint: enable=W0622


def _get_network_io_errors():
    """ Holds IOErrors that should be considered 'recoverable' """
    return (errno.EWOULDBLOCK,
            errno.EAGAIN)

EVENT_SIZE = mmap.ALLOCATIONGRANULARITY
EVENT_FORMAT = "@iLlIIhhh"
FORMAT_SIZE = struct.calcsize(EVENT_FORMAT)
OX_FORMAT_SIZE = 128

logging.basicConfig(level=logging.ERROR)
logger = log.Logger(logger=logging.getLogger(__name__))

class EventFactory(object):
    """ Creates and handles events """
    __metaclass__ = abc.ABCMeta
