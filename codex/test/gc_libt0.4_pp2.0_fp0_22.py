import gc, weakref

def _build_weakref(obj, callback):
    """Build a weak reference to an object with a callback when it dies."""
    def _weakref_cb(obj_ref):
        callback(obj_ref())
    return weakref.ref(obj, _weakref_cb)

class _GCWrapper(object):
    """Wrapper class for objects that have a __del__ method.

    This class is used to make sure that any objects that have a __del__ method
    are not collected by the garbage collector.  This is necessary because the
    __del__ method may be doing something important (like closing a file or
    socket).  The __del__ method will be called when the object is garbage
    collected, but the object will not be collected until after the __del__
    method is called.
    """
    def __init__(self, obj):
        self._obj = obj
        self._weakref = _build_weakref(obj, self._cb)
        self._cb_called = False

