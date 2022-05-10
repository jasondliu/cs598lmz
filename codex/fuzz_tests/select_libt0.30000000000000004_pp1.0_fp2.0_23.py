import selectors
import sys
import types

from . import _util
from . import _util_py2
from . import _util_py3
from . import _util_posix
from . import _util_windows
from . import _winapi

__all__ = (
    'Selector', 'BaseSelector', 'DefaultSelector',
    'EVENT_READ', 'EVENT_WRITE',
    'BaseSelectorEventLoop', 'SelectorEventLoop',
    'SelectorKey', 'BaseSelectorKey',
)

EVENT_READ = selectors.EVENT_READ
EVENT_WRITE = selectors.EVENT_WRITE


class BaseSelectorKey:
    """The key returned by the selector.

    It contains the fileobj, the events to monitor, and the data
    associated to the fileobj.
    """

    __slots__ = ('fileobj', 'fd', 'events', 'data')

    def __init__(self, fileobj, fd, events, data=None):
        self.fileobj = fileobj
        self.fd = f
