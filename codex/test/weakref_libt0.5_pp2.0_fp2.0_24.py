import weakref
from collections import defaultdict
from datetime import datetime
from functools import partial
from itertools import chain

from .. import config
from .. import errors
from .. import events
from .. import futures
from .. import protocols
from .. import tasks
from .. import transports
from .. import utils
from ..log import logger


__all__ = ['BaseEventLoop', 'SelectorEventLoop']


PY_35 = sys.version_info >= (3, 5)
_STOPPED = object()
_CANCELLED_AND_NOTIFIED = object()


class BaseEventLoop(object):
    """Abstract event loop.

    This manages a set of file descriptors.  The event loop can
    be started and stopped and feeds callbacks with file descriptors
    that are ready for some kind of I/O.

    The base class is an abstract subclass and cannot be used directly.
    Use one of the subclasses defined in this module instead.
    """

    def __init__(self, selector=None):
        if selector is None:
            selector = selectors.DefaultSelector()
