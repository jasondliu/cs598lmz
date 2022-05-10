import weakref

class Event(object):
    """
    A simple event class.
    """
    def __init__(self, name):
        self.name = name
        self.callbacks = []
        
    def register(self, callback):
        """
        Register a callback for this event.
        """
        self.callbacks.append(callback)
        
    def unregister(self, callback):
        """
        Unregister a callback for this event.
        """
        self.callbacks.remove(callback)
        
    def fire(self, *args, **kwargs):
        """
        Fire this event, calling all registered callbacks.
        """
        for callback in self.callbacks:
            callback(*args, **kwargs)
            
class EventManager(object):
    """
    A class to manage events.
    """
    def __init__(self):
        self.events = {}
        
    def createEvent(self, name):
        """
        Creates an event with the given name.
        """
        self.events[name] = Event(
