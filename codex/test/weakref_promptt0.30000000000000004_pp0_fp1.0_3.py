import weakref
# Test weakref.ref() with a class that has a custom __hash__() method.

class A(object):
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        return self.x

a = A(42)
r = weakref.ref(a)
