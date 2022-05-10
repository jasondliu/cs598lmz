import gc, weakref, pdb

class WeakBoundMethod (weakref.ref):
    def __new__ (typ, obj, func):
        # Keyword arguments are different.
        args = (func.__self__, func.__func__)
        return weakref.ref.__new__ (typ, args, func)

    def __init__ (self, obj, func):
        self.obj = obj

    def __call__ (self, *args, **kwargs):
        return self.__func__ (self.__self__, *args, **kwargs)

    def __eq__ (self, rhs):
        if isinstance (rhs, type (self)):
            rhs = rhs ()
        return weakref.ref.__eq__ (self, rhs)

    def __ne__ (self, rhs):
        if isinstance (rhs, type (self)):
            rhs = rhs ()
        return weakref.ref.__ne__ (self, rhs)

    def __getattr__ (self, name):
        return getattr (self (), name)


