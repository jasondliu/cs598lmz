import weakref
# Test weakref.ref(self) in a class method

class C:
    def __init__(self):
        self.x = 42

    def f(self):
        return weakref.ref(self)

c = C()
r = c.f()
assert r() is c
del c
assert r() is None
