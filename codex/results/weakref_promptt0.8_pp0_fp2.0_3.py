import weakref
# Test weakref.ref().
import weakref
import gc

class C(object):
    pass

o = C()
r = weakref.ref(o)

assert r() is o

assert set(gc.get_referents(r)) == {r, o}
assert set(gc.get_referrers(r)) == {weakref.ReferenceType}
assert set(gc.get_referrers(o)) == {r, weakref.ReferenceType}

# Test weakref.WeakValueDictionary().
import weakref

class C(object): pass

o = C()

d = weakref.WeakValueDictionary()
d['o'] = o

assert len(d) == 1
assert d['o'] is o


d['o'] = C()

assert len(d) == 0

l = []

def foo(obj):
    l.append(obj)

w = weakref.ref(o, foo)

del o

import gc

gc.collect()

assert len(l) == 1
assert l[0
