import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
assert r() is f

# Test weakref.proxy()

p = weakref.proxy(f)
assert p is f

# Test weakref.getweakrefcount()

assert weakref.getweakrefcount(f) == 1

# Test weakref.getweakrefs()

assert weakref.getweakrefs(f) == [r]

# Test weakref.WeakKeyDictionary()

d = weakref.WeakKeyDictionary()
d[f] = 1
assert d[f] == 1
del f
assert d == {}

# Test weakref.WeakValueDictionary()

d = weakref.WeakValueDictionary()
d[1] = f
assert d[1] is f
del f
assert d == {}

# Test weakref.finalize()

class Foo:
    pass

f = Foo()
finalizer = weakref.finalize(f, lambda: None)
assert finalizer.alive
