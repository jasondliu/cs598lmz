import weakref


class EventHandler(BaseObject):
    """
    An object that handles events.
    """
    __slots__ = ('__weakref__', 'events', 'enabled', 'base_events')

    def __init__(self):
        """
        The constructor takes no parameters.
        """
        global [events, base_events]
        BaseObject.__init__(self)
        events = event_handler.EventHandler()
        base_events = event_handler.EventHandler()
        enabled = True

    def enable_events(self):
        """
        Enable the events.
        """
        global enabled
        enabled = True

    def disable_events(self):
        """
        Disable the events.
        """
        global enabled
        enabled = False

    def is_enabled(self):
        """
        Returns True if the object's event handler is currently enabled, otherwise False
        """
        global enabled
        return enabled

    def on_event(self, event, handler, priority=0):
        """
        Register for a new event.
        :param event: The event
