import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

o2 = C()
r2 = weakref.ref(o2, lambda x: None)
assert r2() is o2

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
assert p is o

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
assert weakref.getweakrefs(o)
