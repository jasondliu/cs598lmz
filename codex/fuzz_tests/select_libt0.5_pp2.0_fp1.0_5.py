import selectors
import sys
import time
import traceback

from . import _core
from . import _events
from . import _util
from . import _util_posix
from . import _util_windows


class Selector:
    """Selector backend.

    This class is considered private to asyncio.
    """

    def __init__(self):
        self._map = {}  # fd -> key
        self._selector = selectors.DefaultSelector()
        self._num_fds = 0

    @property
    def num_fds(self):
        """The number of registered file descriptors."""
        return self._num_fds

    def register(self, fileobj, events, data=None):
        """Register a file object.

        Return a (possibly new) key for the object.

        The file object must be an object with a fileno() method that returns
        a file descriptor.  It can be a regular or an asynchronous file
        descriptor.

        The (possibly new) key is returned.

        """
        key = self._map.get(fileobj
