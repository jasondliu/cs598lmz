import weakref
# Test weakref.ref() with a class that defines __eq__ and __hash__.
# This used to segfault.
class C(object):
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

c = C(1)
r = weakref.ref(c)
