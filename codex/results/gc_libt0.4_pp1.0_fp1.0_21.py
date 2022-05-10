import gc, weakref, sys

class _CachedObject(object):
    def __init__(self, obj):
        self.obj = obj
        self.weakref = weakref.ref(obj)


class _CachedObjects(object):
    def __init__(self):
        self._objects = []

    def add(self, obj):
        self._objects.append(_CachedObject(obj))

    def get(self, obj):
        for cached_obj in self._objects:
            if cached_obj.weakref() == obj:
                return cached_obj.obj


class _ObjectCache(object):
    def __init__(self):
        self._cached_objects = _CachedObjects()

    def add(self, obj):
        self._cached_objects.add(obj)

    def get(self, obj):
        return self._cached_objects.get(obj)


class _ObjectCacheManager(object):
    def __init__(self):
        self._caches = {}

    def get_cache(self, obj):
        cache =
