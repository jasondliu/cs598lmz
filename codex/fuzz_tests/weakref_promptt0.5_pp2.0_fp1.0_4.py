import weakref
# Test weakref.ref(x) returns a weak reference to x.

class C(object):
    pass

o = C()
r = weakref.ref(o)
assert r() is o

r = weakref.ref(o, lambda: None)
assert r() is o

r = weakref.ref(o, lambda x: None)
assert r() is o

r = weakref.ref(o, lambda x, y: None)
assert r() is o

r = weakref.ref(o, lambda x, y, z: None)
assert r() is o

try:
    r = weakref.ref(o, lambda x, y, z, t: None)
except TypeError:
    pass
else:
    assert False, "expected TypeError"

try:
    r = weakref.ref(o, lambda x, y, z, t, u: None)
except TypeError:
    pass
else:
    assert False, "expected TypeError"

try:
    r = weakref.ref(o, lambda x, y, z, t,
