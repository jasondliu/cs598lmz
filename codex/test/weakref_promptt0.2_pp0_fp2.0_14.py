import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
assert r() is f

f = None
assert r() is None

# Test weakref.proxy()

class Foo:
    pass

f = Foo()
p = weakref.proxy(f)
assert p is f

f = None
try:
    p.attr
except ReferenceError:
    pass
else:
    assert False, "expected ReferenceError"

# Test weakref.getweakrefcount()

class Foo:
    pass

f = Foo()
assert weakref.getweakrefcount(f) == 0

r = weakref.ref(f)
assert weakref.getweakrefcount(f) == 1

r2 = weakref.ref(f)
assert weakref.getweakrefcount(f) == 2

r = None
assert weakref.getweakrefcount(f) == 1

r2 = None
assert weakref.getweakrefcount(f) == 0

# Test weakref.getweakrefs
