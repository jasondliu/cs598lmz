import weakref
# Test weakref.ref is callable
try:
    weakref.ref(None)
except TypeError:
    del weakref
    import weakref

if not hasattr(weakref, 'ref'):
    # Python < 2.4
    class WeakMethod:
        __slots__ = ('_obj', '_func_ref')

        def __init__(self, func):
            self._obj = None
            self._func_ref = weakref.ref(func.im_self, self._cleanup)
            self.__name__ = func.__name__

        def __call__(self, *args, **kwargs):
            if self._obj is None:
                return None
            return self._obj(*args, **kwargs)

        def _cleanup(self, ref):
            self._obj = None

    def WeakMethod(func):
        if type(func) is types.MethodType:
            return WeakMethod(func)
        return func
else:
    WeakMethod = weakref.ref

# Python < 2.4 compatibility
