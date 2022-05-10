import weakref
# Test weakref.ref() with a class that has a __del__ method.

class C:
    def __init__(self, x):
        self.x = x
