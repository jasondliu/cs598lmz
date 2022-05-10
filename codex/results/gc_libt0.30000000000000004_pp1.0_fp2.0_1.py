import gc, weakref

#
# The following code is used to keep a cache of previously created objects.
# This can be used to ensure that two objects with the same ID will in fact
# be the same object.
#

class _WeakKeyDictionary(UserDict.UserDict):
    """Mapping class that references keys weakly."""

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        o = self.data[key]()
        if o is None:
            raise KeyError, key
        else:
            return o

    def __setitem__(self, key, item):
        self.data[key] = weakref.ref(item)

    def __delitem__(self, key):
        del self.data[key]

    def keys(self):
        L = []
        for key, wr in self.data.items():
            o = wr()
            if o is not None:
                L.append(key)
        return L

class _WeakValueDictionary(UserDict.UserDict
