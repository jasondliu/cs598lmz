import weakref
# Test weakref.ref(obj)
# Test weakref.proxy(obj)
# Test weakref.getweakrefcount(obj)
# Test weakref.getweakrefs(obj)
# Test weakref.WeakKeyDictionary
# Test weakref.WeakValueDictionary
# Test weakref.WeakSet
# Test weakref.finalize
# Test weakref.ReferenceType
# Test weakref.CallableProxyType
# Test weakref.ProxyType
# Test weakref.ProxyTypes
# Test weakref.WeakMethod
# Test weakref.WeakMethodProxy
# Test weakref.WeakMethodProxyType

# Test weakref.ref(obj)
class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

# Test weakref.proxy(obj)
p = weakref.proxy(o)
assert p is o

# Test weakref.getweakrefcount(obj)
assert weakref.getweakrefcount(o) == 2

# Test weakref.getweakrefs(obj)
assert weakref.getweakrefs(o
