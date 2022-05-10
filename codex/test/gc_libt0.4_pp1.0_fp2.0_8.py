import gc, weakref

#-------------------------------------------------------------------------------

class _WeakMethod(object):
    def __init__(self, method):
        self.method = weakref.ref(method.im_self), method.im_func
    def __call__(self, *args, **kwargs):
        obj, func = self.method
        if obj is not None:
            return func(obj(), *args, **kwargs)

#-------------------------------------------------------------------------------

class _WeakMethodDict(dict):
    def __getitem__(self, key):
        value = super(_WeakMethodDict, self).__getitem__(key)
        if value is None:
            raise KeyError(key)
        return value
    def __setitem__(self, key, value):
        if value is not None:
            value = _WeakMethod(value)
        super(_WeakMethodDict, self).__setitem__(key, value)
    def __delitem__(self, key):
        super(_WeakMethodDict, self).__setitem__(key, None)

#-------------------------------------------------------------------------------

