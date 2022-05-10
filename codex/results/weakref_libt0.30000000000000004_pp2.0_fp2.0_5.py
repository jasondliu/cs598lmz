import weakref

from . import _core
from . import _util
from . import _thread
from . import _weakmethod
from . import _weakref
from . import _weakrefset

_log = _util.get_logger(__name__)


class _LifecycleEvent(object):
    """
    An event that is fired when an object is created or destroyed.
    """

    def __init__(self, obj):
        self.obj = obj


class _LifecycleListener(object):
    """
    A listener for lifecycle events.
    """

    def __init__(self, callback):
        self.callback = callback

    def __call__(self, event):
        self.callback(event.obj)


class _LifecycleEventManager(object):
    """
    A manager for lifecycle events.
    """

    def __init__(self):
        self.listeners = _weakrefset.WeakSet()

    def add_listener(self, listener):
        """
        Add a listener for lifecycle events.

        :param listener:
