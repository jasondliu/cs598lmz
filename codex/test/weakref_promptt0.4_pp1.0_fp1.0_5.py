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
class Foo(object):
    def f(self):
        return 24

x = Foo()
assert x.f() == 24
p = weakref.proxy(x)
assert p.f() == 24
del x
try:
    p.f()
except ReferenceError:
    pass
else:
    raise Exception("expected ReferenceError")

# Test weakref.finalize()
class Foo(object):
    def __init__(self, x):
        self.x = x
    def __del__(self):
        self.x = None

x = Foo(42)
assert x.x == 42
f = weakref.finalize(x, x.x, 42)
assert f.alive
assert x.x == 42
del x
assert not f.alive

# Test weakref.KeyedRef()
