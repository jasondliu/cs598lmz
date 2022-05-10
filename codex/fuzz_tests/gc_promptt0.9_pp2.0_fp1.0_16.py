import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
gc.collect()

l = []
w = weakref.ref(l)
assert w() is l
assert w() is not None
del l
gc.collect()
assert w() is None


class X(object):
    pass

x = X()
w = weakref.ref(x)
assert w() is x
assert w() is not None
del x
gc.collect()
assert w() is None

from weakref import ProxyType
def cb(obj):
    print obj

x = X()
p = ProxyType(x, cb)
assert x is p
assert p.__class__ is X
del x
gc.collect()
