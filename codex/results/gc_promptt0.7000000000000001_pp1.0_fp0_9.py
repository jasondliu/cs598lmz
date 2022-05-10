import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = []
b = a
del a
found = gc.collect()
assert found == 1
# Test gc.garbage
# Create a cycle 'a ---> b ---> a'
class A:
    pass
a = A()
b = A()
a.b = b
b.a = a
del A
# Note that a is still accessible, via gc.garbage!
# Note that we cannot use a or b after gc.collect()!
assert not gc.collect()
assert len(gc.garbage) == 2
# However, gc.garbage contains just weakrefs, so
# the objects may be collected anyway.
# This API is not very useful...
del gc.garbage[:]
del a, b
# Test gc.get_referrers
a = []
# Get all objects that directly refer to a.
found = gc.get_referrers(a)
assert len(found) == 1
assert found[0] is __builtins__.globals()
# Test gc.get_referents

