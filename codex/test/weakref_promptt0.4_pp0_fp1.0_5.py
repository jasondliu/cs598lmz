import weakref
# Test weakref.ref()
import _weakref

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o
assert r() is not None
assert _weakref.getweakrefcount(o) == 1
assert _weakref.getweakrefs(o) == [r]

# Test weakref.proxy()
p = weakref.proxy(o)
assert p is o
assert p is not None
assert _weakref.getweakrefcount(o) == 1
assert _weakref.getweakrefs(o) == [r]

# Test weakref.ref(<weakref>)
r2 = weakref.ref(r)
assert r2() is r
assert r2() is not None
assert _weakref.getweakrefcount(r) == 1
assert _weakref.getweakrefs(r) == [r2]

# Test weakref.proxy(<weakref>)
p2 = weakref.proxy(r)
assert p2 is r
assert p2 is not None
assert _weakref.getweakref
