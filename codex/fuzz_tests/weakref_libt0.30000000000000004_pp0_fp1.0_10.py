import weakref

from . import _core
from . import _util
from . import _thread
from . import _weakmethod

from . import _core
from . import _util
from . import _thread
from . import _weakmethod

_log = _util.get_logger(__name__)


class _Event(object):
    """
    An event object.

    This object is used to synchronize threads. An event manages an internal
    flag that can be set to true with the set() method and reset to false with
    the clear() method. The wait() method blocks until the flag is true.
    """

    def __init__(self):
        self._flag = False
        self._cond = _thread.Condition()

    def is_set(self):
        """Return true if and only if the internal flag is true."""
        return self._flag

    def set(self):
        """Set the internal flag to true.

        All threads waiting for it to become true are awakened. Threads
        that call wait() once the flag is true will not block at all.
        """
        with
