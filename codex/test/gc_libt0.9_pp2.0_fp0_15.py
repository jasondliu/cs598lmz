import gc, weakref, os

class CachedObject:
    def __init__(self, obj, filename=None):
        self.obj = obj
        self.filename = filename

def DefaultCache(createfunc, filename, lru):
    def _cache(objreturned):
        cachedref = lru.get(filename, None)
        if cachedref and cachedref() is not None:
            obj = cachedref()
