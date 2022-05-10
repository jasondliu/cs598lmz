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

o = C()
r = weakref.ref(o)
assert r() is o

r2 = weakref.ref(o)
assert r2() is o

del o
assert r() is None
assert r2() is None

# Test weakref.proxy

import weakref

class C(object):
    pass

o = C()
p = weakref.proxy(o)
assert p is o

del o
assert not hasattr(p, 'x')

try:
    p.x
except ReferenceError:
    pass
else:
    assert False, "reference should have gone away"

try:
    p.x = 42
except ReferenceError:
    pass
else:
    assert False, "reference should have gone away"

# test weakref.WeakSet
import weakref

class C(object):
    pass

o
