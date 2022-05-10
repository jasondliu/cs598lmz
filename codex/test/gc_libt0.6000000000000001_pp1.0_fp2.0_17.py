import gc, weakref
import logging

class WeakKeyDictionary(object):
    def __init__(self):
        self.d = weakref.WeakKeyDictionary()

    def __getitem__(self, key):
        return self.d[key]

    def __setitem__(self, key, value):
        self.d[key] = value

    def __delitem__(self, key):
        del self.d[key]

    def __iter__(self):
        return iter(self.d)

    def __contains__(self, key):
        return key in self.d

    def __len__(self):
        return len(self.d)

    def __str__(self):
        return str(self.d)

    def __repr__(self):
        return repr(self.d)

    def __eq__(self, other):
        if not isinstance(other, WeakKeyDictionary):
            return False
        return self.d == other.d

