import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test weakref.ref()
class Foo:
    pass

f = Foo()
r = weakref.ref(f)
f2 = r()
assert f is f2

# Test weakref.proxy()
p = weakref.proxy(f)
assert f is p

# Test weakref.getweakrefcount()
assert weakref.getweakrefcount(f) == 1

# Test weakref.getweakrefs()
assert weakref.getweakrefs(f) == [r]

# Test weakref.WeakKeyDictionary()
d = weakref.WeakKeyDictionary()
d[f] = 42
assert d[f] == 42

# Test weakref.WeakValueDictionary()
d = weakref.WeakValueDictionary()
d[42] = f
assert d[42] is f

# Test weakref.finalize()
class Foo:
    pass

f = Foo()
r = weakref.finalize(f, lambda: None)
assert r.alive
del f
gc.collect
