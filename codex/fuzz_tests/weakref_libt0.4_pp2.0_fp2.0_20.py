import weakref

class WeakMethod(object):
    def __init__(self, method):
        self.method = method.im_func
        self.obj = weakref.ref(method.im_self)

    def __call__(self, *args, **kwargs):
        obj = self.obj()
        if obj is None:
            return None
        return self.method(obj, *args, **kwargs)

class WeakMethodBound(object):
    def __init__(self, method):
        self.method = method.im_func
        self.obj = weakref.ref(method.im_self)

    def __call__(self, *args, **kwargs):
        obj = self.obj()
        if obj is None:
            return None
        return self.method(obj, *args, **kwargs)

class WeakMethodUnbound(object):
    def __init__(self, method):
        self.method = method

    def __call__(self, *args, **kwargs):
        obj = self.obj()
        if obj is None
