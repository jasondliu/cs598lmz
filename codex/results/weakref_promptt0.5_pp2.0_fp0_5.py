import weakref
# Test weakref.ref()

import weakref
import gc

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

o2 = C()
r2 = weakref.ref(o2, lambda x: x)
assert r2() is o2
assert r2() is not None

o = C()
p = C()
o.x = p
r = weakref.ref(p)
del o, p
gc.collect()
assert r() is None

o = C()
p = C()
o.x = p
r = weakref.ref(p, lambda x: x)
del o, p
gc.collect()
assert r() is None

# Test weakref.proxy()

import weakref

class C:
    pass

o = C()
o.x = 1
r = weakref.proxy(o)
assert r.x == 1

o2 = C()
o2.x = 1
r2 = weakref.proxy(o2, lambda x: x)
assert
