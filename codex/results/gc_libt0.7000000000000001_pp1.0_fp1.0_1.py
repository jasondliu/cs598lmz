import gc, weakref, collections

def _string_to_weakref(s):
    if isinstance(s, str):
        return weakref.ref(s)
    elif isinstance(s, weakref.ref):
        return s
    else:
        raise TypeError("strings or weakrefs only please")

class CacheEntry(object):
    __slots__ = ('ref', 'obj', 'ctime', 'mtime')

    def __init__(self, ref, obj, ctime, mtime):
        self.ref = ref
        self.obj = obj
        self.ctime = ctime
        self.mtime = mtime

    def __repr__(self):
        return "<%s %r>" % (self.__class__.__name__, self.ref())

class LRUDict(dict):
    """A dict that keeps only the N most recently used entries

    >>> d = LRUDict(2)
    >>> d['a'] = 1
    >>> d['b'] = 2
    >>> d['c'] = 3
    >>> d['d'] =
