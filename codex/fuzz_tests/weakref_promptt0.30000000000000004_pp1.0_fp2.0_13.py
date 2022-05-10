import weakref
# Test weakref.ref()

class C:
    pass

c = C()
r = weakref.ref(c)
assert r() is c
c2 = C()
r2 = weakref.ref(c2)
assert r2() is c2

# Test weakref.proxy()
p = weakref.proxy(c)
assert p is c
assert type(p) is C
assert type(r) is weakref.ReferenceType

# Test weakref.getweakrefcount()
assert weakref.getweakrefcount(c) == 2

# Test weakref.getweakrefs()
assert weakref.getweakrefs(c) == [r, p]

# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
d[c] = 1
assert d[c] == 1
assert len(d) == 1

# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
d[1] = c
assert d[1] is c
assert len(d) == 1

# Test weakref.final
