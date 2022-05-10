import gc, weakref

def _get_dict(obj):
    try:
        return object.__getattribute__(obj, '__dict__')
    except AttributeError:
        raise TypeError("%s is not a dictproxy instance" % obj)

def _make_weakref(target):
    return weakref.ref(target, lambda weak, name=target.__name__:
                                  getattr(gc.get_referents(weak)[0], name).__del__())

class _weakmethod:
    """Helper for implementing weak methods"""

    __slots__ = "key", "meth"

    def __init__(self, meth):
        self.key = _make_weakref(meth.__self__)
        self.meth = meth.__func__

    def __call__(self, *args, **kwargs):
        self_obj = self.key()
        if self_obj is None:
            raise ReferenceError("weakly-referenced object no longer exists")
        return self.meth(self_obj, *args, **kwargs)
