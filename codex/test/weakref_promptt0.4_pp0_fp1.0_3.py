import weakref
# Test weakref.ref() and weakref.proxy()

import weakref
import gc

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o
assert r() is not None

p = weakref.proxy(o)
assert p is o

o2 = C()
r2 = weakref.ref(o2)
assert r2() is o2
assert r2() is not None

o2 = None
gc.collect()
assert r2() is None

# Test weakref.finalize()

import weakref
import gc

class C:
    pass

o = C()

def callback(wr, o=o):
    print('callback', wr, o)

r = weakref.finalize(o, callback)
assert r.alive

o = None
gc.collect()
assert not r.alive

# Test weakref.WeakKeyDictionary

import weakref

d = weakref.WeakKeyDictionary()
o = C()
d[o] = 1
