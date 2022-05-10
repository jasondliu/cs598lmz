import gc, weakref

class _WeakKeyDictionary(UserDict.UserDict):

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        o = self.data[key()]
        return o

    def __setitem__(self, key, item):
        self.data[key()] = item

    def __delitem__(self, key):
        del self.data[key()]

    def __repr__(self):
        return repr(self.data)

    def __cmp__(self, dict):
        return cmp(self.data, dict)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

    def copy(self):
        return self.data.copy()

    def has_key(self, key):
        return self.data.has_key(key)

    def update(self, dict):
        self.data.update(dict)

    def keys(self):
       
