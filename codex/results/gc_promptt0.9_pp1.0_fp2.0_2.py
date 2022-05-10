import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
gc.collect()
# Test gc.get_objects
gc.get_objects()
# Test gc.get_referrers
gc.get_referrers(w)
# Test gc.get_referents
gc.get_referents(w)

##############################################################################

# Verify that weakrefs don't hold their referents alive
garbage = []
def callback(ignored):
    print "Cannot access the callback's argument"
wr = weakref.ref(garbage, callback)
del garbage
gc.collect()
print wr()

# verify weakref doesn't keep objects alive
class C(object):
    pass

c = C()
wr = weakref.ref(c)
assert wr() is c
del c
gc.collect()
assert wr() is None
del wr
gc.collect()
