import gc, weakref

class Cached(object):
    __slots__ = ("__weakref__", "__cache__")
    def __init__(self):
        object.__setattr__(self, "__cache__", weakref.WeakValueDictionary())
    def __get__(self, obj, cls):
        if obj is None:
            return self
        try:
            return self.__cache__[obj]
        except KeyError:
            value = self.__cache__[obj] = self.__get__(obj, cls)
            return value
    def __getattr__(self, name):
        raise AttributeError(name)

class C(object):
    @Cached
    def spam(self):
        print "creating spam"
        return 42

if __name__ == "__main__":
    x = C()
    y = C()
    print x.spam()
    print y.spam()
    del x
    del y
    gc.collect()
    x = C()
    print x.spam()
