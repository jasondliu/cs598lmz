import gc, weakref

class WeakMethod(object):
    """
    A proxy for bound methods that ensures that the method is never called
    with a dead instance.
    """
    def __init__(self, fn):
        self._weakref = weakref.ref(fn.im_self)
        self._func = fn.im_func
        self._name = fn.im_func.__name__
        self._class = fn.im_class

    def __call__(self, *args, **kwargs):
        inst = self._weakref()
        if inst is None:
            raise ReferenceError('weakly-referenced object no longer exists')
        return self._func(inst, *args, **kwargs)

    def __hash__(self):
        return hash(self._weakref())

    def __eq__(self, other):
        if isinstance(other, WeakMethod):
            return (other._func == self._func and
                    other._weakref() == self._weakref())
        return NotImplemented

    def __ne__(self, other):
        if is
