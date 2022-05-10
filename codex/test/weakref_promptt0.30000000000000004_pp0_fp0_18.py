import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
assert r() is f
assert r() is not None
del f
assert r() is None

# Test weakref.proxy()

f = Foo()
p = weakref.proxy(f)
assert p is f
assert p is not None
del f
try:
    p.foo
except ReferenceError:
    pass
else:
    raise Exception("expected ReferenceError")

# Test weakref.getweakrefcount()

assert weakref.getweakrefcount(Foo) == 0
f = Foo()
assert weakref.getweakrefcount(f) == 0
r = weakref.ref(f)
assert weakref.getweakrefcount(f) == 1
p = weakref.proxy(f)
assert weakref.getweakrefcount(f) == 2
del r
assert weakref.getweakrefcount(f) == 1
del p
assert weakref.getweakrefcount(f) == 0

# Test weakref.getweakrefs()
