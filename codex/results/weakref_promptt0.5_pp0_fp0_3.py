import weakref
# Test weakref.ref() to an instance method

class C:
    def f(self):
        return 42

c = C()
r = weakref.ref(c.f)
assert r() == 42

class D:
    def __init__(self):
        self.f = lambda: 42

d = D()
r = weakref.ref(d.f)
assert r() == 42

class E:
    def __init__(self):
        self.f = 42

e = E()
r = weakref.ref(e.f)
assert r() == 42

# Test weakref.ref() to a built-in function
import math
r = weakref.ref(math.atan2)
assert r() == math.atan2

# Test weakref.ref() to a built-in method
r = weakref.ref(math.atan2.__doc__.split)
assert r() == math.atan2.__doc__.split

# Test weakref.ref() to a function
def f():
    pass
r = weakref.ref(f)
