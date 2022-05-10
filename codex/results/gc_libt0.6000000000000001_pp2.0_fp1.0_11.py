import gc, weakref

class WeakCallable(object):
    def __init__(self, func):
        self.weak_self = None
        self.func = func
        self.name = func.__name__
    def __call__(self, *args, **kwargs):
        if self.weak_self:
            return self.func(self.weak_self(), *args, **kwargs)
        else:
            return self.func(*args, **kwargs)
    def __get__(self, obj, type=None):
        self.weak_self = weakref.ref(obj)
        return self
    def __repr__(self):
        return f"WeakCallable({self.func})"

class WeakMethod(object):
    def __init__(self, method):
        self.weak_self = None
        self.method = method
        self.name = method.__name__
    def __call__(self, *args, **kwargs):
        if self.weak_self:
            return self.method(self.weak_self(), *args, **
