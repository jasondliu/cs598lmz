import weakref

class Event(object):
    """Base class for all events"""
    def __init__(self, event_type):
        self.type = event_type

class QuitEvent(Event):
    """Event to quit the game"""
    def __init__(self):
        Event.__init__(self, QUIT)

class InputEvent(Event):
    """Event to provide input to the game"""
    def __init__(self, input_type, key, repeat_count=0):
        Event.__init__(self, input_type)
        self.key = key
        self.repeat_count = repeat_count

class EventManager(object):
    """EventManager class"""
    def __init__(self):
        self._listeners = {}
        for event_type in EVENTS:
            self._listeners[event_type] = []

    def register_listener(self, event_type, listener):
        """Add a listener to the list of listeners for the given event type"""
        if event_type not in EVENTS:
            raise ValueError("Unknown event type
