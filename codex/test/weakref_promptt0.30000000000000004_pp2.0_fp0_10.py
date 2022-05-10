import weakref
# Test weakref.ref

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

o2 = C()
r.__init__(o2)
assert r() is o2

# Test weakref.proxy

o = C()
p = weakref.proxy(o)
assert p is o

o2 = C()
p.__init__(o2)
assert p is o2

# Test weakref.getweakrefcount

o = C()
assert weakref.getweakrefcount(o) == 0

r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1

p = weakref.proxy(o)
assert weakref.getweakrefcount(o) == 2

# Test weakref.getweakrefs

o = C()
assert weakref.getweakrefs(o) == []

r = weakref.ref(o)
assert weakref.getweakrefs(o) == [r]

