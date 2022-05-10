import weakref

from . import _py2to3
from . import _threads
from . import _util
from . import _vendor
from . import _weakref

_logger = _util.get_logger(__name__)


class _Base(object):
    """Base class for all objects that can be registered with the hub.

    This class is not intended to be used directly.
    """

    def __init__(self):
        # The hub that this object is registered with, or None if it is not
        # registered.
        self._hub = None

        # A weakref to this object.
        self._ref = None

    def __del__(self):
        # If this object is still registered with a hub when it is deleted,
        # then unregister it.
        if self._hub is not None:
            self._hub.unregister(self)

    def _set_hub(self, hub):
        """Set the hub that this object is registered with.

        This method should only be called by the hub itself.
        """
