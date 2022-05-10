import gc, weakref, sys

class WeakValueDictionary(dict):
    def __init__(self, dict=None, **kwds):
        self.update(dict, **kwds)

    def __getitem__(self, key):
        o = dict.__getitem__(self, key)()
        if o is not None:
            return o
