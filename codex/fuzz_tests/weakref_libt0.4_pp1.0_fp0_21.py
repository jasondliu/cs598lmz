import weakref

from . import _base


class _WeakKeyDictionary(_base.WeakKeyDictionary):
    def __init__(self):
        self._d = weakref.WeakKeyDictionary()

    def __getitem__(self, key):
        return self._d[key]

    def __setitem__(self, key, value):
        self._d[key] = value

    def __delitem__(self, key):
        del self._d[key]

    def __contains__(self, key):
        return key in self._d

    def get(self, key, default=None):
        return self._d.get(key, default)

    def pop(self, key, default=None):
        return self._d.pop(key, default)

    def setdefault(self, key, default=None):
        return self._d.setdefault(key, default)

    def __iter__(self):
        return iter(self._d)

    def __len__(self):
        return len(self._d)

    def __repr__
