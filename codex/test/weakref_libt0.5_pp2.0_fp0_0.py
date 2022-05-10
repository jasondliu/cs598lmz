import weakref

class WeakMethod(object):
    """
    Copied from http://code.activestate.com/recipes/81253/
    """
    def __init__(self, f):
        try:
            self.f = weakref.ref(f.im_func)
            self.c = weakref.ref(f.im_self)
        except AttributeError:
            self.f = weakref.ref(f)
            self.c = None

    def __call__(self):
        if self.c is not None:
            return self.f()(self.c())
        else:
            return self.f()

class WeakMethodBound(object):
    """
    Copied from http://code.activestate.com/recipes/81253/
    """
    def __init__(self, f, c):
        self.f = weakref.ref(f)
        self.c = weakref.ref(c)

    def __call__(self):
        return self.f()(self.c())

