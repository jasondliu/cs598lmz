import gc, weakref, sys

class WeakValueDictionary(dict):
    def __init__(self, dict=None, **kwds):
        self.update(dict, **kwds)

    def __getitem__(self, key):
        o = dict.__getitem__(self, key)()
        if o is not None:
            return o
        raise KeyError, key

    def __contains__(self, key):
        try:
            o = dict.__getitem__(self, key)()
        except KeyError:
            return False
        return o is not None

    __marker = object()
    def pop(self, key, default=__marker):
        if default is self.__marker:
            return dict.pop(self, key)()
        else:
            return dict.pop(self, key, default)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def setdefault(self, key, default=None):
        try:
            return
