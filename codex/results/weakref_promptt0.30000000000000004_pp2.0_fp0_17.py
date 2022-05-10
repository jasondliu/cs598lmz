import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o
del o
assert r() is None

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
assert p.__class__ is weakref.ProxyType
assert p is o
del o
try:
    p.foo
except ReferenceError:
    pass
else:
    raise Exception("should have raised ReferenceError")

# Test weakref.getweakrefcount()

o = C()
assert weakref.getweakrefcount(o) == 0
r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1
p = weakref.proxy(o)
assert weakref.getweakrefcount(o) == 2
del r, p
assert weakref.getweakrefcount(o) == 0

# Test weakref.getweakrefs()

o = C()
assert weakref.getweakrefs(o) == []
r = weakref.ref(
