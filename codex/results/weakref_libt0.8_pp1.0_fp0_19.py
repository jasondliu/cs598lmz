import weakref


class Reference(ReferenceType):
    """
    This class wraps a weak reference, proxying most attribute lookups to the
    weakly referenced object.  Instances of this class are callable, and
    will proxy calls to the weakly referenced object.
    """

    def __init__(self, ob):
        self.__weakref = weakref.ref(ob)

    def proxy(self):
        return self.__weakref()

    def __getattr__(self, name):
        ob = self.proxy()
        if ob is None:
            raise ReferenceError("weakly-referenced object no longer exists")
        return getattr(ob, name)

    __str__ = lambda self: str(self.proxy())
    __hash__ = lambda self: hash(self.proxy())
    __nonzero__ = lambda self: self.proxy() is not None
    __bool__ = lambda self: self.proxy() is not None
    __len__ = lambda self: len(self.proxy())
    __repr__ = lambda self: repr(self.proxy())

    def __
