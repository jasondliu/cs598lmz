import socket
import sys
import threading
import time
import traceback

from . import _util
from . import _winapi
from . import constants
from . import events
from . import futures
from . import protocols
from . import transports
from .log import logger


__all__ = ['BaseEventLoop', 'SelectorEventLoop', 'ProactorEventLoop',
           '_ProactorBasePipeTransport', '_ProactorReadPipeTransport',
           '_ProactorWritePipeTransport', '_ProactorSocketTransport',
           '_SelectorSocketTransport', '_SelectorDatagramTransport',
           '_SelectorTransport', '_UnixSelectorEventLoop']


class BaseEventLoop(object):
    """Abstract event loop.

    This manages a set of file descriptors.  For each file descriptor
    it manages, it calls a read or write handler when the descriptor
    is ready for reading or writing respectively.

    The event loop has a 'clock' which is a monotonic time.  The
    'call_at' and 'call_later' methods can be used to
