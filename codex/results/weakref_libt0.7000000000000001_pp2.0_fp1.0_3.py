import weakref

__all__ = ['CachedType']

class CachedType(object):
    def __new__(cls, *args, **kwargs):
        try:
            return cls._cache[args][kwargs]
        except KeyError:
            if not hasattr(cls, '_cache'):
                cls._cache = weakref.WeakValueDictionary()
            if args not in cls._cache:
                cls._cache[args] = weakref.WeakValueDictionary()
            new = super(CachedType, cls).__new__(cls, *args, **kwargs)
            cls._cache[args][kwargs] = new
            return new
