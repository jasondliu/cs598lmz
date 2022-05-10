import weakref
# Test weakref.ref() with a callable object.

class A:
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

a = A(10)
r = weakref.ref(a)
