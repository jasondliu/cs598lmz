import weakref
# Test weakref.ref / .ProxyType round-trip.
# Create a weak reference to a type and verify that
# the returned weak reference is a type.

class A(object):
    pass

def f():
    pass

class B(A):
    pass

class C(object):
    pass

for o in (A, B, C, A, A(), f, 42, 42.0001, "foo"):
    r = weakref.ref(o)
    p = r()
    assert type(p) is type(o), "%s, %s" % (type(p), type(o))
    assert p is o, "%s, %s"%(p, o)
