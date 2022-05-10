import weakref

class WeakMethod(object):
    def __init__(self, method):
        self.method = weakref.ref(method)

    def __call__(self, *args, **kwargs):
        if self.method() is None:
            return
        return self.method()(*args, **kwargs)

class WeakMethodBound(object):
    def __init__(self, method):
        self.method = weakref.ref(method)

    def __call__(self, *args, **kwargs):
        if self.method() is None:
            return
        return self.method()(*args, **kwargs)

class WeakMethodFree(object):
    def __init__(self, method):
        self.method = weakref.ref(method.im_func)
        self.instance = weakref.ref(method.im_self)

    def __call__(self, *args, **kwargs):
        if self.method() is None:
            return
        return self.method()(self.instance(), *args, **kwargs)


