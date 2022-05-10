import weakref
import time
import threading

from .logger import logger
from .utils import run_async_method_in_loop
from .events import Event, EventHandler
from . import devices
from .exceptions import InvalidParameterError


class _DeviceManagerListener(object):
    def __init__(self):
        super(_DeviceManagerListener, self).__init__()

        self.event_handlers = []
        self.event_handler_lock = threading.Lock()

    @property
    def event_handler_count(self):
        with self.event_handler_lock:
            return len(self.event_handlers)

