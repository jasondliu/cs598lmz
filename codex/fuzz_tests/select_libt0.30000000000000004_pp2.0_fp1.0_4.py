import select
import socket
import sys
import time
import traceback

from . import _common
from . import _constants
from . import _util
from . import _util_posix
from . import _util_windows
from . import _winapi


class _SelectorKey(_common.SelectorKey):
    """A key returned by `selectors.Selector.select()`.

    This class is intended to be private to the `selectors` module.

    """

    def __init__(self, selector, fileobj, fd, events, data):
        super().__init__(selector, fileobj, events, data)
        self._fd = fd

    def __repr__(self):
        info = [
            ("fileobj", self._fileobj),
            ("fd", self._fd),
            ("events", self._events),
            ("data", self._data),
        ]
        return "{}({})".format(self.__class__.__name__,
                               ", ".join(("{}={!r}".format(k, v)) for k,
