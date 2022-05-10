import weakref

from . import base
from . import events
from . import _util

class InputDevice(base.Device):
    """
    Base class for input devices.
    """
    def __init__(self, device_id, name, description):
        base.Device.__init__(self, device_id, name, description)
        self._event_queue = collections.deque()

    @property
    def event_queue(self):
        """
        Returns the event queue.
        """
        return self._event_queue

    def _process_event(self, event):
        """
        Processes an event.
        """
        self._event_queue.append(event)

    def _process_events(self):
        """
        Processes all queued events.
        """
        while self._event_queue:
            event = self._event_queue.popleft()
            self._dispatch_event(event)

    def _dispatch_event(self, event):
        """
        Dispatches an event.
        """
        if isinstance(event
