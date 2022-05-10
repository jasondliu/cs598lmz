import weakref
# Test weakref.ref()

class C(object):
    pass

c = C()
r = weakref.ref(c)
assert r() is c

# Test weakref.proxy()

c = C()
p = weakref.proxy(c)
assert p is c

# Test weakref.getweakrefcount()

c = C()
assert weakref.getweakrefcount(c) == 0

r = weakref.ref(c)
assert weakref.getweakrefcount(c) == 1

p = weakref.proxy(c)
assert weakref.getweakrefcount(c) == 2

# Test weakref.getweakrefs()

c = C()
assert weakref.getweakrefs(c) == []

r = weakref.ref(c)
assert weakref.getweakrefs(c) == [r]

p = weakref.proxy(c)
assert weakref.getweakrefs(c) == [r, p]

# Test weakref.ReferenceType

c = C()
r = weakref.ref
