import weakref
# Test weakref.ref()
import _weakref

class C(object):
    pass

o = C()
r = weakref.ref(o)
assert r() is o
assert r() is not None
assert r() is not 42

# Test weakref.proxy()
p = weakref.proxy(o)
assert p is o
assert p is not None
assert p is not 42

# Test weakref.getweakrefcount()
assert weakref.getweakrefcount(o) == 1
assert weakref.getweakrefcount(p) == 1

# Test weakref.getweakrefs()
assert weakref.getweakrefs(o) == [r]
assert weakref.getweakrefs(p) == [r]

# Test weakref.ReferenceType
assert isinstance(r, weakref.ReferenceType)
assert not isinstance(p, weakref.ReferenceType)

# Test weakref.ProxyType
assert not isinstance(r, weakref.ProxyType)
assert isinstance(p, weakref.ProxyType)

# Test weakref.CallableProxyType
