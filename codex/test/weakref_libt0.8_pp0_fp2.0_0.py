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
