import gc, weakref

class WeakMethod(object):
    def __init__(self, method):
        self.method = weakref.ref(method)
    def __call__(self, *args, **kwargs):
        method = self.method()
        if method is None:
            return None
        else:
            return method(*args, **kwargs)

class WeakMethodBound(object):
    def __init__(self, method):
        self.method = weakref.ref(method.__self__)
        self.func = method.__func__
    def __call__(self, *args, **kwargs):
        method = self.method()
        if method is None:
            return None
        else:
            return self.func(method, *args, **kwargs)

def WeakMethodFactory(method):
    if inspect.ismethod(method):
        return WeakMethodBound(method)
    else:
        return WeakMethod(method)

class WeakMethodBound(object):
    def __init__(self, method):
        self.method = weakref.
