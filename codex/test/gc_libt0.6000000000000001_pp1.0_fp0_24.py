import gc, weakref, types

#------------------------------------------------------------------------------
class _WeakMethod(object):
    def __init__(self, method):
        self._method = weakref.ref(method.im_self)
        self._func = method.im_func
        self._class = method.im_class

    def __call__(self, *args, **kwargs):
        obj = self._method()
        if obj is not None:
            return self._func.__get__(obj, self._class)(*args, **kwargs)
        else:
            return None

#------------------------------------------------------------------------------
class WeakMethod(object):
    def __init__(self, method):
        if type(method) == types.MethodType:
            self.proxy = _WeakMethod(method)
        else:
            self.proxy = weakref.proxy(method)

#------------------------------------------------------------------------------
class WeakIdentityDictionary(object):
    def __init__(self):
        self.data = {}
        self.removed = []

    def __contains__(self, key): return key in self.data
