import gc, weakref, re

#------------------------------------------------------------------------------
#
#  The class below is used to ensure that a given callback is called only once
#  for a given event.  This is sometimes necessary in order to avoid problems
#  caused by circular references.
#
#------------------------------------------------------------------------------

class EventHandler:
    """ A class that is used to ensure that a given callback is called only
        once for a given event.  This is sometimes necessary in order to avoid
        problems caused by circular references.
    """

    def __init__(self, callback):
        """ Initialize the event handler.
        """
        self.callback = callback
        self.weak_callbacks = {}

    def __call__(self, *args, **kw):
        """ Invoke the callback, if it hasn't already been invoked for this
            event.
        """
        # Create a weak reference to the callback, and use it as the key.
        key = weakref.ref(self.callback)

        # If the weak reference is not already in the dictionary, then this is
        # the first time the callback has been invoked for this event, so
       
