import weakref

class CachedType(type):
    def __init__(cls, name, bases, dct):
        super(CachedType, cls).__init__(name, bases, dct)
        cls._cache = weakref.WeakValueDictionary()
    def __call__(cls, *args):
        if args in cls._cache:
            return cls._cache[args]
        else:
            obj = super(CachedType, cls).__call__(*args)
            cls._cache[args] = obj
            return obj

class Cached(object):
    __metaclass__ = CachedType
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Cached(%r)' % self.name

if __name__ == '__main__':
    a = Cached('a')
    b = Cached('b')
    x = Cached('x')
    y = Cached('y')
    z = Cached('z')
