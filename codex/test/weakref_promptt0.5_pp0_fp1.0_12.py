import weakref
# Test weakref.ref()
def f():
    return 42

x = f()
assert x == 42
r = weakref.ref(x)
assert r() is x
del x
assert r() is None
# Test weakref.proxy()
class Foo:
    def __init__(self, x):
        self.x = x

x = Foo(42)
assert x.x == 42
r = weakref.proxy(x)
assert r.x == 42
del x
try:
    r.x
except ReferenceError:
    pass
