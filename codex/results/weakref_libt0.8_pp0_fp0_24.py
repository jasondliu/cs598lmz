import weakref

class Event(object):
    """
    
    The base class from which all other events are derived.
    
    """
    def __init__(self, source, target):
        self._source = source
        self._target = target
    
    @property
    def target(self):
        """
        
        The target object that is to be notified of the event.
        
        """
        return self._target() if isinstance(self._target, weakref.ReferenceType) else self._target
    
    @property
    def source(self):
        """
        
        The object that is the source of the event.
        
        """
        return self._source() if isinstance(self._source, weakref.ReferenceType) else self._source


class EventListener(object):
    """
    
    
    
    """
    def __init__(self):
        super(EventListener, self).__init__()
    
    def notify(self, event):
        """
        
        Notify this listener of the event.
        
        :param event:
