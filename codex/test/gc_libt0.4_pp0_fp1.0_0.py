import gc, weakref

def _weak_ref(obj, callback):
    """
    Return a weak reference to obj, with a callback to call when obj
    dies.  If the object has an __on_del__ method, it will be called
    when the object is about to be finalized; otherwise, the callback
    will be called with no arguments.  If the object is already dead,
    the callback is called immediately.
    """
    def _callback(ref):
        try:
            if hasattr(obj, "__on_del__"):
                obj.__on_del__()
            else:
                callback()
        except ReferenceError:
            pass # Ignore errors in the callback
    wr = weakref.ref(obj, _callback)
    if wr() is None:
        _callback(wr)
    return wr

