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
else:
    raise Exception, "expected a ReferenceError"
# Test weakref.getweakrefcount()
x = Foo(42)
assert weakref.getweakrefcount(x) == 0
r = weakref.ref(x)
assert weakref.getweakrefcount(x) == 1
r2 = weakref.ref(x)
assert weakref.getweakrefcount(x) == 2
del r
assert weakref.getweakrefcount(x) == 1
del r2
assert weakref.getweakrefcount(x) ==
