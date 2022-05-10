import weakref
import threading

from threading import current_thread

from .base import BaseObject
from . import signals
from . import events
from . import exceptions
from . import util

from . import log
log = log.getLogger('core.devices.base')


class BaseDevice(BaseObject):
    """
    Base class for all devices.
    """

    DEVICE_TYPE = None

    DEVICE_INSTANCE_ID = None

    def __init__(self, *args, **kwargs):
        super(BaseDevice, self).__init__(**kwargs)

        self._connected = False

        self._device_type = self.DEVICE_TYPE
        self._device_instance_id = self.DEVICE_INSTANCE_ID

        self._connection_lock = threading.RLock()
        self._current_connection = None
        self._connection_threads = weakref.WeakSet()

        self._events = events.EventDispatcher(self)

        # Device state
        self.state = {}

    def __repr__(self):
        return
