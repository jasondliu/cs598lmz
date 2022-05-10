import weakref

class WeakMethod(object):
    def __init__(self, f):
        self.f = weakref.ref(f.im_func)
        self.c = weakref.ref(f.im_self)

    def __call__(self, *args, **kwargs):
        c = self.c()
        f = self.f()
        if c is not None and f is not None:
            return f(c, *args, **kwargs)
        else:
            return None

class WeakMethodBound(object):
    def __init__(self, f):
        self.f = weakref.ref(f.im_func)
        self.c = weakref.ref(f.im_self)

    def __call__(self, *args, **kwargs):
        c = self.c()
        f = self.f()
        if c is not None and f is not None:
            return f(c, *args, **kwargs)
        else:
            return None

class WeakMethodUnbound(object):
    def __
