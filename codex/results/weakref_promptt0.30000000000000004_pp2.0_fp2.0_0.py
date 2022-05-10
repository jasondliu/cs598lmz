import weakref
# Test weakref.ref()
def f():
    return 42

x = f()
assert x == 42
r = weakref.ref(x)
assert r() == 42
del x
assert r() == 42

# Test weakref.proxy()
class Foo:
    def __init__(self, x):
        self.x = x
    def f(self):
        return self.x

x = Foo(42)
assert x.f() == 42
r = weakref.proxy(x)
assert r.f() == 42
del x
try:
    r.f()
except ReferenceError:
    pass
else:
    raise Exception("expected ReferenceError")

# Test weakref.getweakrefcount()
class Foo:
    pass

x = Foo()
assert weakref.getweakrefcount(x) == 0
r = weakref.ref(x)
assert weakref.getweakrefcount(x) == 1
r2 = weakref.ref(x)
assert weakref.getweakrefcount(x) == 2
del r
assert weakref.getweakrefcount
