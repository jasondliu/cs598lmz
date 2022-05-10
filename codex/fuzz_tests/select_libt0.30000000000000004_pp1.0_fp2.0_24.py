import select
import socket
import sys
import threading
import time

from . import _common
from . import _util
from . import _util_posix
from . import _util_windows
from . import constants
from . import errors
from . import events
from . import futures
from . import selector_events
from . import transports
from .log import logger


__all__ = ['BaseEventLoop', 'SelectorEventLoop']


class BaseEventLoop(object):
    """Abstract event loop.

    This manages a set of file descriptors and their associated tasks and
    callbacks.

    The event loop is built on top of a selector and basically runs a
    selector.select() loop forever.

    When a file descriptor is ready, it runs all the tasks and callbacks
    registered for the fd.

    Methods on this class should not be called directly.  Instead, use the
    call_soon(), call_later(), call_at() methods.

    Subclasses should override the following methods:
        _run_once
        _process_events
        _selector_class
    """

    def __init__
