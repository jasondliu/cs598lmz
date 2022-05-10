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

# Test weakref.getweakrefcount()

o = C()
assert weakref.getweakrefcount(o) == 0
r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1

# Test weakref.getweakrefs()

o = C()
assert weakref.getweakrefs(o) == []
r = weakref.ref(o)
assert weakref.getweakrefs(o) == [r]

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()
o = C()
d[o] = 1
assert d[o] == 1
del o
gc.collect()
assert len(d) == 0

# Test weakref.WeakValueDictionary

d = weakref.WeakValueD
