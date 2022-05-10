import weakref

class WeakKeyDictionary(dict):
    """Mapping class that references keys weakly."""
    def __init__(self, *args, **kwargs):
        super(WeakKeyDictionary, self).__init__(*args, **kwargs)
        self.__weakref__ = weakref.proxy(self)

    def __getitem__(self, key):
        return super(WeakKeyDictionary, self).__getitem__(weakref.ref(key))

    def __setitem__(self, key, value):
        super(WeakKeyDictionary, self).__setitem__(weakref.ref(key), value)

    def __delitem__(self, key):
        super(WeakKeyDictionary, self).__delitem__(weakref.ref(key))

    def __contains__(self, key):
        return super(WeakKeyDictionary, self).__contains__(weakref.ref(key))

    def get(self, key, default=None):
        return super(WeakKeyDictionary, self).get(weakref.ref(key
