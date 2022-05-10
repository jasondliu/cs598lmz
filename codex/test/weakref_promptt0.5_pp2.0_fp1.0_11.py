import weakref
# Test weakref.ref() with a class that overrides __eq__ and __hash__

class C(object):
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

a = C(1)
b = C(2)

r = weakref.ref(a)

