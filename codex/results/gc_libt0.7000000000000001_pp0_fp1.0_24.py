import gc, weakref
import logging
log = logging.getLogger(__name__)

class Wrapper(object):
    """
    A weak reference to an object, with a callback when the object is
    deleted.
    """
    def __init__(self, obj, callback):
        self.obj = obj
        self.callback = callback
        self.weakref = weakref.ref(obj, self.on_delete)
        
    def on_delete(self, ref):
        self.callback(ref)

    def __call__(self, *args, **kwargs):
        """
        Call the object.

        Keep the object alive for this time.
        """
        return self.obj(*args, **kwargs)

    def __repr__(self):
        return '<Wrapper: %r>' % (self.obj, )

    def __getattr__(self, attr):
        """
        Pass unknown attributes to the object.
        """
        return getattr(self.obj, attr)

class Watchdog(object):
    """
    A watchdog for
