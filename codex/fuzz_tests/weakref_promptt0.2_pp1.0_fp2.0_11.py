import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
assert r() is f
assert r() is not None

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
    p
except ReferenceError:
    pass
else:
    raise Exception("expected ReferenceError")

# Test weakref.getweakrefcount()

class Foo:
    pass

f = Foo()
assert weakref.getweakrefcount(f) == 0

r = weakref.ref(f)
assert weakref.getweakrefcount(f) == 1

p = weakref.proxy(f)
assert weakref.getweakrefcount(f) == 2

f = None
assert weakref.getweakrefcount(r()) == 0
assert weakref.getweakrefcount(p) == 0

# Test weakref.getweakrefs()


