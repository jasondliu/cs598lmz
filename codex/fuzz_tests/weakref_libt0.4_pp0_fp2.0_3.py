import weakref

class _Callback(object):
    """
    Callback class for a single callback.
    """
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs
        self.enabled = True
        self.ref = weakref.ref(callback)
        
    def __call__(self, *args, **kwargs):
        """
        Call the callback.
        """
        if self.enabled:
            self.callback(*self.args, **self.kwargs)
            
    def __eq__(self, other):
        """
        Check if two callbacks are equal.
        """
        return self.callback == other.callback
    
    def __hash__(self):
        """
        Return a hash of the callback.
        """
        return hash(self.callback)
    
    def __str__(self):
        """
        Return the callback as a string.
        """
        return str(self.callback)
    
    def __re
