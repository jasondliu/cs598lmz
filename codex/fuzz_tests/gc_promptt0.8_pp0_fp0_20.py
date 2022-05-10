import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs

class C(object):
    pass

def make_circular():
    a = C()
    a.a = a
    return a

def make_weakref(obj):
    w = weakref.ref(obj)
    assert w() is obj
    gc.collect()
    return w

a = make_circular()
w = make_weakref(a)
# The following is important to make the second test work.
# The first time it runs, a will be collected and a
# negative number will be printed.  The second time around,
# the negative number will already be cached and will be
# immediately returned, and a will not be collected.
gc.collect()
print gc.collect()
del a
gc.collect()
assert w() is None
assert w() is None

a = make_circular()
w = make_weakref(a)
gc.collect()
del a
a = make_circular()
print gc.collect()
del a
assert w() is None
assert w() is None
