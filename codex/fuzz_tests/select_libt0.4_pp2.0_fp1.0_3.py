import select

from . import _util
from . import _event
from . import _core
from . import _selector
from . import _selectors

__all__ = ['BaseEventLoop', 'SelectorEventLoop', '_UnixSelectorEventLoop']


class BaseEventLoop(object):
    """Base class for event loops.

    This class is considered internal and should not be used in user code.
    """

    def __init__(self, selector=None):
        self._selector = selector or _selectors.DefaultSelector()
        self._clock = _util.MonotonicClock()
        self._scheduled = []
        self._ready = collections.deque()
        self._stopping = False
        self._thread_id = None

        self._exception_handler = None
        self._slow_callback_duration = None
        self._slow_callback_duration_warning = None
        self._slow_callback_duration_warning_task = None

    def close(self):
        """Close the loop.

        This clears the queues and shuts down the executor, if any.
