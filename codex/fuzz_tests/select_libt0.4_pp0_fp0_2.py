import select
import sys
import threading
import time
import traceback
import warnings

from . import _compat
from . import _dummy_thread
from . import _event
from . import _util
from . import _weakref
from . import events
from . import futures
from . import protocols
from . import tasks
from .log import logger
from .transports import _BaseTransport


__all__ = ['BaseEventLoop', 'BaseProactorEventLoop', 'BaseSelectorEventLoop',
           'SelectorEventLoop', 'ProactorEventLoop', 'EventLoopPolicy',
           'AbstractEventLoop']


class _TimerHandle(_BaseTimerHandle):
    __slots__ = ['_loop', '_callback', '_args', '_cancelled']

    def __init__(self, when, callback, args, loop):
        super().__init__(when)
        self._loop = loop
        self._callback = callback
        self._args = args
        self._cancelled = False

    def __repr__(self):
        res = super().__repr__()

