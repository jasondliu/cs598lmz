import weakref
# Test weakref.ref() with a callable object.

class C(object):
    def __init__(self, n):
        self.n = n
    def __call__(self):
        return self.n

def f(x):
    return x

def g(x):
    return x()

for n in [0, 1, 2]:
    c = C(n)
    r = weakref.ref(c)
    assert r() is c
    assert g(r) == n
    del c
    assert r() is None
    assert g(r) is None

r = weakref.ref(f)
assert r() is f
assert g(r) is f
del f
