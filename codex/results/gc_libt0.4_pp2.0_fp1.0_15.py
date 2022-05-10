import gc, weakref

class WeakMethod(object):
    def __init__(self, func):
        self.func = func.im_func
        self.obj = func.im_self
        self.cls = func.im_class
    def __call__(self, *args, **kw):
        if self.obj is not None:
            return self.func(self.obj, *args, **kw)
        else:
            return self.func(*args, **kw)
    def __eq__(self, other):
        return self.func == getattr(other, "im_func", None) and \
               self.obj == getattr(other, "im_self", None) and \
               self.cls == getattr(other, "im_class", None)
    def __ne__(self, other):
        return not self.__eq__(other)

class WeakMethodBound(WeakMethod):
    def __eq__(self, other):
        return self.func == getattr(other, "im_func", None) and \
               self.cls == get
