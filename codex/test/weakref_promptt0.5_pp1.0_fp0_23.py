import weakref
# Test weakref.ref() with a class that has a __del__ method.

class Foo:
    def __init__(self, name):
        self.name = name
