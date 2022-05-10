import weakref

class _Cache(object):
    """
    Cache instance.
    """
    def __init__(self, max_size=None, max_age=None, min_age=None, max_items=None, min_items=None):
        self.max_size = max_size
        self.max_age = max_age
        self.min_age = min_age
        self.max_items = max_items
        self.min_items = min_items
        self._cache = {}
        self._size = 0
        self._age = 0

    def get(self, key):
        """
        Get item from cache.
        """
        if key in self._cache:
            item = self._cache[key]
            if item.expired:
                del self._cache[key]
            else:
                return item.value
        return None

    def set(self, key, value):
        """
        Add item to cache.
        """
        if key in self._cache:
            item = self._cache[key]
