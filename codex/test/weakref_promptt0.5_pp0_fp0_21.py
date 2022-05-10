import weakref
# Test weakref.ref
import weakref

class C(object):
    pass

o = C()
r = weakref.ref(o)
assert r() is o

del o
assert r() is None

# Test weakref.proxy
import weakref

class C(object):
    pass

o = C()
p = weakref.proxy(o)
assert p is o

del o
try:
    p
    assert False
except ReferenceError:
    pass

# Test weakref.getweakrefcount
import weakref

class C(object):
    pass

o = C()
assert weakref.getweakrefcount(o) == 0

# Test weakref.getweakrefs
import weakref

class C(object):
    pass

o = C()
assert weakref.getweakrefs(o) == []

# Test weakref.WeakKeyDictionary
import weakref

d = weakref.WeakKeyDictionary()

class C(object):
    pass

o = C()
d[o] = 1
