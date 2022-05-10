import weakref
# Test weakref.ref() with a class that has a __del__ method.

class Foo:
    def __init__(self, i):
        self.i = i
        self.d = weakref.ref(self)

