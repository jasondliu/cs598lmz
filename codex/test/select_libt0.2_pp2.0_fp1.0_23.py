import select
import sys
import time
import traceback

from . import _util
from . import _winapi
from . import constants
from . import events
from . import futures
from . import locks
from . import protocols
from . import tasks
from . import transports
from .log import logger


__all__ = ('BaseEventLoop', 'SelectorEventLoop', 'ProactorEventLoop',
           'NewSelectorEventLoop', 'NewProactorEventLoop', 'DefaultEventLoopPolicy')


class _UnixSelectorEventLoop(selectors.BaseSelector):
    """Selector event loop for UNIX systems."""

    def __init__(self, selector):
        super().__init__(selector)
