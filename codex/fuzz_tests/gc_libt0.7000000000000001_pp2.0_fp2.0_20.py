import gc, weakref

class WeakNotifier(object):
    """
    A property that does not have a reference to the object it is
    notifying, allowing for garbage collection of the object.
    """

    __slots__ = ('_func', '_args', '_kwargs', '_observe_func')

    def __init__(self, func, *args, **kwargs):
        super(WeakNotifier, self).__init__()
        self._func = func
        self._args = args
        self._kwargs = kwargs
        self._observe_func = None

    def _is_dead(self):
        return self._func is None

    def _dispatch(self, obj):
        if self._func is not None:
            self._func(obj, *self._args, **self._kwargs)

    def __call__(self, obj):
        self._dispatch(obj)

    def _observe(self, obj):
        if self._observe_func is not None:
            self._observe_func(obj)

