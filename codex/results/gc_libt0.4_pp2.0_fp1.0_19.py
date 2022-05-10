import gc, weakref

class WeakValueDictionary(UserDict.UserDict):
    """Mapping class that references values weakly.

    Entries in the dictionary will be discarded when no strong
    reference to the value exists anymore
    """

    def __init__(self, dict=None):
        self.data = {}
        if dict is not None:
            self.update(dict)

    def __getitem__(self, key):
        o = self.data[key]()
        if o is None:
            raise KeyError, key
        else:
            return o

    def __repr__(self):
        return repr(self.data)

    def __setitem__(self, key, value):
        self.data[key] = weakref.ref(value)

    def __delitem__(self, key):
        del self.data[key]

    def copy(self):
        new = WeakValueDictionary()
        for key, wr in self.data.items():
            o = wr()
            if o is not None:
                new[key] = o

