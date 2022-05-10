import weakref
import time


class _CacheItem(object):
    def __init__(self, key, value, timeout):
        self.key = key
        self.value = value
        self.timeout = timeout
        self.t = 0

    def __repr__(self):
        return '<CacheItem key={}, value={}, timeout={}>'.format(
            self.key, self.value, self.timeout)


class TimeoutDict(dict):
    def __init__(self, timeout=60):
        self._timeout = timeout
        self._refs = {}

    def __getitem__(self, key):
        if key in self:
            item = super(TimeoutDict, self).__getitem__(key)
            self._refs[key].t += self._timeout
            return item.value
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        if key not in self:
            self._refs[key] = _CacheItem(key, value, self._timeout)
            super(
