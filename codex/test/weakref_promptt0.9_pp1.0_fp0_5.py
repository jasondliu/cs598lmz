import weakref
# Test weakref.ref_create.

# Make a base class will instances of which are not weakly referencable.
# There is no such built-in base class, so create one.
import UserDict
class Dict2(UserDict.DictMixin):
    def __init__(self):
        self.data = {}
    def __setitem__(self, key, item):
        self.data[key] = item
    def __getitem__(self, key):
        return self.data[key]
    def __delitem__(self, key):
        del self.data[key]
    def keys(self):
        return self.data.keys()

# Test an instance of this class.
import sys
d = Dict2()
r = weakref.ref(d)
