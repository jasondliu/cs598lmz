import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)


class Event(object):
    """
    Event is a simple class that wraps around an SDL event.
    """
    def __init__(self, event):
        self.type = event.type
        self.name = event.type.name
        self.event = event
        self._dict = {}

    def __repr__(self):
        return "<Event: %s>" % self.name

    def __getitem__(self, key):
        if key not in self._dict:
            self._dict[key] = getattr(self.event, key)
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value
        setattr(self.event, key, value)


class EventDispatcher(object):
    """
    EventDispatcher is a simple class that handles dispatching
    of events to their respective handlers.
    """
    def __init__(self):
        self._handlers = {}
        self._default_handler = None

    def __repr__
