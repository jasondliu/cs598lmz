import weakref
# Test weakref.ref(x)

class C(object):
    pass

o = C()
r = weakref.ref(o)
assert r() is o

o2 = C()
r2 = weakref.ref(o2, lambda x: None)
assert r2() is o2

# Test weakref.proxy(x)

o = C()
p = weakref.proxy(o)
assert p.__class__ is weakref.ProxyType
assert p is o

o2 = C()
p2 = weakref.proxy(o2, lambda x: None)
assert p2.__class__ is weakref.ProxyType
assert p2 is o2

# Test weakref.getweakrefcount(x)

assert weakref.getweakrefcount(C()) == 0

# Test weakref.getweakrefs(x)

assert weakref.getweakrefs(C()) == []

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()
o1 = C()
o2 = C()
o3 = C
