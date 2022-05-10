import weakref
# Test weakref.ref()
class Foo:
    pass

f = Foo()
r = weakref.ref(f)

assert r() is f

# Test weakref.proxy()
r = weakref.proxy(f)

assert r is f

# Test weakref.getweakrefcount()
r = weakref.ref(f)

assert weakref.getweakrefcount(f) == 1

# Test weakref.getweakrefs()
r = weakref.ref(f)

assert weakref.getweakrefs(f) == [r]

# Test weakref.WeakKeyDictionary()
class Foo:
    pass

f = Foo()
d = weakref.WeakKeyDictionary()
d[f] = 1

assert d[f] == 1

del f

assert d == {}

# Test weakref.WeakValueDictionary()
class Foo:
    pass

f = Foo()
d = weakref.WeakValueDictionary()
d[1] = f

assert d[1] is f

del f

assert d ==
