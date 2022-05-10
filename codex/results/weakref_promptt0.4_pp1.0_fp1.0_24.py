import weakref
# Test weakref.ref() and weakref.proxy().
import gc

class C(object):
    pass

o = C()
r = weakref.ref(o)
assert r() is o
assert weakref.getweakrefcount(o) == 1
assert weakref.getweakrefs(o) == [r]

p = weakref.proxy(o)
assert p is o
assert weakref.getweakrefcount(o) == 2
assert weakref.getweakrefs(o) == [r, p]

r2 = weakref.ref(o)
assert r2() is o
assert weakref.getweakrefcount(o) == 3
assert weakref.getweakrefs(o) == [r, p, r2]

p2 = weakref.proxy(o)
assert p2 is o
assert weakref.getweakrefcount(o) == 4
assert weakref.getweakrefs(o) == [r, p, r2, p2]

# Test weakref.proxy() with a tuple.
t = (1, 2, 3)

