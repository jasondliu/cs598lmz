import gc, weakref

from . import _pytest

class WeakKeyDictionary:
    """A weak-key dictionary."""

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        o = self.data[key]()
        if o is None:
            raise KeyError, key
        else:
            return o

    def __setitem__(self, key, value):
        self.data[key] = weakref.ref(value)

    def __delitem__(self, key):
        del self.data[key]

    def __contains__(self, key):
        try:
            o = self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __repr__(self):
        return "<WeakKeyDictionary at %s>" % hex(id(self))

    def __len__(self):
        return
