import gc, weakref

#
#   This is a simple implementation of a weak reference dictionary.
#   It is used to store the mapping between the Python objects
#   and the C++ objects.
#

class WeakValueDictionary(object):
    def __init__(self):
        self.d = weakref.WeakValueDictionary()
    def __getitem__(self, key):
        return self.d[key]
    def __setitem__(self, key, value):
        self.d[key] = value
    def __contains__(self, key):
        return key in self.d
    def __delitem__(self, key):
        del self.d[key]
    def __len__(self):
        return len(self.d)
    def __iter__(self):
        return iter(self.d)
    def __repr__(self):
        return repr(self.d)
    def __str__(self):
        return str(self.d)
    def get(self, key, default=None):
        return self.d.get
