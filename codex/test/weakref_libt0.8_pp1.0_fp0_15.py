import weakref

class _RefCache(object):

    def __init__(self):
        self._cache = {}

    def __contains__(self, obj):
        """If an object is a weakref proxy object, it contains the
        weakref.
        """
        return self.get(obj) is not None

    def set(self, obj, value):
        """Save a reference to the value with weakref to obj."""
        self._cache[weakref.ref(obj)] = value

    def get(self, obj):
        """If the object is a weakref proxy object, return the
        weakref.
        """
        try:
            return self._cache[weakref.ref(obj)]
        except KeyError:
            return None

    def remove(self, obj):
        """If the object is a weakref proxy object, remove it."""
        try:
            del self._cache[weakref.ref(obj)]
        except KeyError:
            pass

    def clear(self):
        """Clear the cache."""
        self._cache.clear()

