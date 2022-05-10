import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

# Test weakref.proxy()

p = weakref.proxy(o)
assert p is o

# Test weakref.getweakrefcount()

assert weakref.getweakrefcount(o) == 1

# Test weakref.getweakrefs()

assert weakref.getweakrefs(o) == [r]

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()
d[o] = 1
assert d[o] == 1
del o
assert len(d) == 0

# Test weakref.WeakValueDictionary

d = weakref.WeakValueDictionary()
d[1] = o
assert d[1] is o
del o
assert len(d) == 0

# Test weakref.WeakSet

s = weakref.WeakSet()
s.add(o)
assert o in s
del o
assert len(s) == 0

#
