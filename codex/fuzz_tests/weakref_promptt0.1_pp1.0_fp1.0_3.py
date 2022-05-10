import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
assert p.__class__ is weakref.ProxyType
assert p is o

# Test weakref.getweakrefcount()

o = C()
assert weakref.getweakrefcount(o) == 0
r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1
p = weakref.proxy(o)
assert weakref.getweakrefcount(o) == 2

# Test weakref.getweakrefs()

o = C()
assert weakref.getweakrefs(o) == []
r = weakref.ref(o)
assert weakref.getweakrefs(o) == [r]
p = weakref.proxy(o)
assert weakref.getweakrefs(o) == [r, p]

# Test weakref.ReferenceType

o = C()
