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
assert p is o
assert p.__class__ is C

# Test weakref.getweakrefcount()

o = C()
assert weakref.getweakrefcount(o) == 0
r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1
r2 = weakref.ref(o)
assert weakref.getweakrefcount(o) == 2

# Test weakref.getweakrefs()

o = C()
assert weakref.getweakrefs(o) == []
r = weakref.ref(o)
assert weakref.getweakrefs(o) == [r]
r2 = weakref.ref(o)
assert weakref.getweakrefs(o) == [r, r2]

# Test weakref.finalize()

# Test weakref
