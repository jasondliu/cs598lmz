import select
import socket
import sys

from . import events
from . import protocol
from . import util
from . import _util
from . import _exceptions
from . import _socketpair


__all__ = ['BaseEventLoop', 'SelectorEventLoop', '_UnixSelectorEventLoop',
           '_WindowsSelectorEventLoop', '_SelectorSocketTransport',
           '_SelectorDatagramTransport', '_SelectorSslTransport']


class BaseEventLoop(events.AbstractEventLoop):
    """Base event loop.

    This class is intended to be used as a base class for concrete
    implementations of the event loop.

    It is not supposed to be instantiated directly.

    This class implements the infrastructure for the event loop, but does not
    implement any policy.  A concrete subclass should implement a policy.

    Notes on thread safety: the event loop is not thread-safe and should not be
    shared among threads.  In general, methods on the event loop should not be
    called while other threads are running, unless it is under the control of
    the event loop itself.
    """

