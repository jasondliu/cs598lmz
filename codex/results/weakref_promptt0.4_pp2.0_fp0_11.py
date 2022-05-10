import weakref
# Test weakref.ref()
def f():
    return 42

x = f()
assert isinstance(x, int)
r = weakref.ref(x)
assert isinstance(r, weakref.ReferenceType)
assert r() is x
assert r() == 42
del x
assert r() is None

# Test weakref.proxy()
class A:
    def __init__(self, x):
        self.x = x

a = A(42)
assert isinstance(a, A)
p = weakref.proxy(a)
assert isinstance(p, weakref.ProxyType)
assert p.x == 42
assert p.x is a.x
del a
try:
    p.x
except ReferenceError:
    pass
else:
    assert False, "expected ReferenceError"

# Test weakref.getweakrefcount()
assert weakref.getweakrefcount(42) == 0
assert weakref.getweakrefcount(f) == 0
assert weakref.getweakrefcount(A) == 0
assert weakref.getweakrefcount(a) == 0
