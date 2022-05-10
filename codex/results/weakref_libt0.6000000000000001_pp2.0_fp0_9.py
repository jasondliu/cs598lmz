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

    def _get_event_handler(self, event_handler_id):
        with self.event_handler_lock:
            for event_handler in self.event_handlers:
                if event_handler.id == event_handler_id:
                    return event_handler
            return None

    def add_event_handler(self, event_handler):
        with self.event_handler_lock:
            self.event_handlers.append(event
